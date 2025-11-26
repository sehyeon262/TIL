T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]

    # 상부터 시계방향으로
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    cnt = 0
    result = 0  # 경우의 수
    for i in range(N):
        for j in range(N):
            for di, dj in dir:
                for c in range(1, N):
                    dx = i + di * c
                    dy = j + dj * c
                    if board[i][j] == 0 and (0 <= dx < N) and (0 <= dy < N):
                        if board[dx][dy] == 0:
                            continue
                        else:
                            break
                        board[i][j] = 1
                        cnt += 1
                    else:
                        break
            if cnt == N:
                result += 1
            else:
                break

    print(f'#{test_case} {result}')

