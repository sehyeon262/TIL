T = int(input())

# ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸
for test_case in range(1, 1+T):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = 'NO'

    # 오른쪽, 아래, 대각선 아래, 대각선 위
    dir = [[0, 1], [1, 0], [1, 1], [-1, 1]]


    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for dx, dy in dir:
                    cnt = 1

            else:
                cnt = 0
        if cnt == 5:
            result = 'YES'
        else:
            result = 'NO'

    # 열
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[j][i] == 'o':
                cnt += 1
            else:
                cnt = 0
        if cnt == 5:
            result = 'YES'
        else:
            result = 'NO'

    # 대각선
    up_cnt = 0
    down_cnt = 0
    for i in range(N):
        if board[i][i] == 'o':
            down_cnt += 1
        else:
            down_cnt = 0

        if board[N-1-i][i] == 'o':
            up_cnt += 1
        else:
            up_cnt = 0
    if up_cnt == 5 or down_cnt == 5:
        result = 'YES'
    else:
        result = 'NO'

    print(f'#{test_case} {result}')


