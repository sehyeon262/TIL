T = int(input())

for test_case in range(1, T+1):
    # 전구 X : A ~ B초, 전구 Y : C ~ D초
    A, B, C, D = map(int, input().split())
    # max => 겹치는 구간 시작
    # min => 겹치는 구간 끝
    # 겹치는 부분 있는 경우
    if min(B, D) - max(A, C) > 0:
        result = min(B, D) - max(A, C)
    else:
        result = 0
    
    print(f'#{test_case} {result}')
