# 1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.
# 2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

# 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램
T = int(input())

for test_case in range(1, T+1):
    arr = list(input())

    opened = 0    # 열린 괄호
    ans = 0     # 잘린 막대 개수

    for i in range(len(arr)):
        # 열린 괄호가 나왔을 때
        if arr[i] == '(':
            opened += 1
        # 닫힌 괄호가 나왔을 때
        else:
            # 직전이 '('이면 레이저임!
            if arr[i-1] == '(':
                opened -=1
                ans += opened
            # 직전이 ')'이면
            else:
                # 열린 괄호가 하나 사라지고, 마지막 조각이 1개 생김
                opened -= 1
                ans += 1
    print(f'#{test_case} {ans}')
