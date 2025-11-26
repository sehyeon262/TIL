T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 원소의 합
    sum_v = 0
    for i in range(N):
        for j in range(N):
            sum_v += arr[i][j]









    '''
    # p[i] : i행에서 선탟한 열번호
    s = 0 # 원소의 합
    for o in range(N):
        s += A[i][p[i]]

    if min_v > s:
        min_v = s
    '''