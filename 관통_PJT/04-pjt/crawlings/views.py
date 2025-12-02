from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .crawlers import fetch_visible_comments
import json
# Create your views here.
def index(request):
    
    return render(request, 'crawlings/index.html')

def search(request):
    company_name = request.POST.get('name')
    stock_code, comments = fetch_visible_comments(company_name)

    stock = Stock.objects.create(name=company_name, code = stock_code, comment = json.dumps(comments, ensure_ascii=False))
    comments_list = json.loads(stock.comment)

    context = {
        "stock": stock,
        "comments": comments_list,
    }
    return render(request, "crawlings/result.html", context)

def delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":        # 안전을 위해 POST로만 삭제
        stock.delete()
        return redirect('crawlings:index')
    # GET으로 들어오면 목록으로 돌려보내거나 확인 페이지를 렌더링해도 됩니다.
    return redirect('crawlings:index')

def delete_comment(request, stock_id, idx):
    stock = get_object_or_404(Stock, pk=stock_id)
    comments = json.loads(stock.comment or '[]')

    if request.method == "POST" and 0 <= idx < len(comments):
        comments.pop(idx)                     # ← idx번째 댓글만 제거
        stock.comment = json.dumps(comments, ensure_ascii=False)
        stock.save(update_fields=['comment'])

    # 검색 결과 화면과 동일한 컨텍스트로 재렌더
    return render(request, "crawlings/result.html", {
        "stock": stock,
        "comments": comments,  })