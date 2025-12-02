from django.shortcuts import render, redirect
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openai import OpenAI
from .models import StockData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserInterestStock

# ---- Selenium Chrome 설정 ----
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 필요시 활성화 가능
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")

chrome_driver_path = settings.BASE_DIR / \
    "chromedriver-win64" / "chromedriver.exe"
service = Service(executable_path=str(chrome_driver_path))

# ---- OpenAI Client ----
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_comment(prompt, model="gpt-5-nano"):
    """OpenAI 모델을 사용해 댓글 분석"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"오류 발생: {e}"


def fetch_stock_and_comments(driver, company_name, limit=20, max_scroll=10):
    """
    Toss Invest:
    1) 사이트 접속
    2) 검색창 활성화 → 회사 검색 (ENTER로 바로 첫 번째 결과 진입)
    3) /order URL에서 종목 코드 추출
    4) /community 이동 → 댓글 최대 20개 수집
    """
    try:
        # 1) 사이트 접속
        print("[DEBUG] 메인 페이지 이동")
        driver.get("https://www.tossinvest.com/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 2) 검색창 활성화
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys("/")
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
            )
        )
        search_input.click()
        search_input.clear()
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.ENTER)
        print(f"[DEBUG] 검색어 입력 및 첫 결과 선택 완료: {company_name}")

        # 3) /order 페이지 로딩 대기
        WebDriverWait(driver, 15).until(EC.url_contains("/order"))
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        current_url = driver.current_url
        print(f"[DEBUG] /order 페이지 진입: {current_url}")

        # 종목 코드 추출
        parts = current_url.split("/")
        stock_code = None
        if "stocks" in parts:
            idx = parts.index("stocks")
            if idx + 1 < len(parts):
                stock_code = parts[idx + 1]

        # 4) 커뮤니티 페이지로 이동
        community_url = f"https://www.tossinvest.com/stocks/{stock_code}/community"
        driver.get(community_url)
        print(f"[DEBUG] 커뮤니티 페이지 이동: {community_url}")

        # 댓글 영역 로딩 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main article"))
        )

        # 5) 댓글 수집 (스크롤 반복 + 누적)
        comments = []
        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        for _ in range(max_scroll):
            # 현재 화면의 댓글 추출
            spans = driver.find_elements(
                By.CSS_SELECTOR, "article.comment span.tw-1r5dc8g0._60z0ev1")
            for span in spans:
                text = span.text.strip()
                if text and text not in comments:
                    comments.append(text)

            if len(comments) >= limit:
                break

            # 스크롤 다운
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        print(f"[DEBUG] 댓글 {len(comments)}개 수집 완료")
        return stock_code, company_name, comments[:limit]

    except Exception as e:
        import traceback
        print("fetch_stock_and_comments 에러:", traceback.format_exc())
        raise


def analyze_comments(comments, company_name):
    """댓글을 GPT 모델로 분석"""
    if comments:
        combined_comments = "\n".join(comments)
        prompt = f"다음은 {company_name}에 대한 댓글들입니다. 종합적인 분석을 한글로 작성하고, 마지막 줄에는 여론을 긍정적, 부정적, 중립으로 판단해 주세요:\n{combined_comments}"
        return ask_comment(prompt)
    return "댓글을 찾을 수 없습니다."


def stock_finder(request, stock_name=None):
    # GET 요청 처리 (프로필에서 종목명 클릭 시)
    if request.method == 'GET' and stock_name:
        company_name = stock_name
    # POST 요청 처리 (메인 검색창에서 검색 시)
    elif request.method == 'POST':
        company_name = request.POST.get('company_name', '').strip()
    # 그 외의 경우 (단순 페이지 첫 접속)
    else:
        return render(request, 'contentfetch/stock_finder.html')

    if not company_name:
        return render(request, 'contentfetch/stock_finder.html', {'error_message': "회사 이름을 입력하세요."})

    # DB 캐시 확인
    try:
        existing_data = StockData.objects.get(
            company_name__iexact=company_name)
        return render(request, 'contentfetch/stock_finder.html', {
            'company_name': existing_data.company_name,
            'stock_code': existing_data.stock_code,
            'comments': existing_data.comments.split("\n") if existing_data.comments else [],
            'chatgpt_response': existing_data.analysis,
            'is_existing_data': True,
        })
    except StockData.DoesNotExist:
        # 데이터가 없으면 크롤링 진행
        pass

    # 크롤링 로직은 기존과 거의 동일하나, 로딩 페이지를 거치지 않고 바로 결과를 보여주는 방식으로 단순화
    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        stock_code, fetched_company_name, comments = fetch_stock_and_comments(
            driver, company_name)
        chatgpt_response = analyze_comments(comments, fetched_company_name)

        stock_data = StockData(
            company_name=fetched_company_name,
            stock_code=stock_code,
            comments="\n".join(comments),
            analysis=chatgpt_response
        )
        stock_data.save()

        return render(request, 'contentfetch/stock_finder.html', {
            'company_name': fetched_company_name,
            'stock_code': stock_code,
            'comments': comments,
            'chatgpt_response': chatgpt_response,
            'is_existing_data': False,
        })
    except Exception as e:
        return render(request, 'contentfetch/stock_finder.html', {'error_message': f"처리 중 오류 발생: {e}"})
    finally:
        if driver:
            driver.quit()


def delete_comment(request):
    """DB에서 댓글 삭제 후 ChatGPT 재분석"""
    if request.method == "POST":
        stock_code = request.POST.get('stock_code')
        comment_index = request.POST.get('comment_index')

        if stock_code and comment_index is not None:
            try:
                comment_index = int(comment_index)
                stock_data = StockData.objects.get(stock_code=stock_code)

                if stock_data:
                    comments = stock_data.comments.split("\n")
                    if 0 <= comment_index < len(comments):
                        # 댓글 삭제
                        del comments[comment_index]
                        stock_data.comments = "\n".join(comments)

                        # ChatGPT 응답 재분석
                        chatgpt_response = analyze_comments(
                            comments, stock_data.company_name)
                        stock_data.analysis = chatgpt_response
                        stock_data.save()

                        return render(request, 'contentfetch/stock_finder.html', {
                            'company_name': stock_data.company_name,
                            'stock_code': stock_data.stock_code,
                            'comments': comments,
                            'chatgpt_response': chatgpt_response,
                        })
            except ValueError:
                pass

                # 에러 시에도 redirect (에러 메시지 대신 기본 화면)
        return redirect("/stock_finder/")

    # GET 요청이면 그냥 stock_finder 페이지로 이동
    return redirect("/stock_finder/")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 사용자를 db에 저장함
            user = form.save()
            # 가입 성공 시 자동 로그인
            auth_login(request, user)
            # 메인 페이지로 이동
            return redirect('contentfetch:stock_finder')
    else:
        form = UserCreationForm()
    return render(request, 'contentfetch/signup.html', {'form': form})


@login_required
def profile(request):
    stocks = UserInterestStock.objects.filter(user=request.user)
    context = {'stocks': stocks}
    return render(request, 'contentfetch/profile.html', context)


@login_required
def add_stock(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stock_name')
        if stock_name and not UserInterestStock.objects.filter(user=request.user, stock_name=stock_name).exists():
            UserInterestStock.objects.create(
                user=request.user, stock_name=stock_name)
    return redirect('contentfetch:profile')


@login_required
def delete_stock(request, stock_pk):
    stock = UserInterestStock.objects.get(pk=stock_pk)
    if request.user == stock.user:
        stock.delete()
    return redirect('contentfetch:profile')
