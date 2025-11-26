# ① 1일 이용권 : 1일 이용이 가능하다.

# ② 1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.

# ③ 3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
#       (11월, 12월에도 3달 이용권을 사용할 수 있다 
#         / 다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)

# ④ 1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

# 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.

# 종료조건: 12월을 모두 고려한 경우
# 가지의 수: 4개 (1일, 1달, 3달, 1년)
def recur(month, total):
    global min_ans

    if month > 12:
        min_ans = min(min_ans, total)   # 최소값 갱신
        return

    # 1일권으로 다 사는 경우
    recur(month + 1, total + (days[month] * day))
    # 1달권으로 다 사는 경우
    recur(month + 1, total + month)
    # 3달권으로 다 사는 경우 
    recur(month + 3, total + month3)
    # 1년 이용권으로 사는 경우
    recur(month + 12, total + year)


T = int(input())
for test_case in range(1, T+1):
    # 이용한 가격들 (1일, 1달, 3달, 1년)
    day, month, month3, year = map(int, input().split())
    # 12개월 이용 계획 (1부터 쓴다)
    days = [0] + list(map(int, input().split()))
    min_ans = float('inf')  # 나올 수 있는 최대금액으로 초기화 (다 1일권으로 구매)
    recur(1, 0) # 1월부터 시작
    print(f'#{test_case} {min_ans}')

# --------- dp 이용 ----------
