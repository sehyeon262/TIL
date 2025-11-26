T = int(input())

# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for test_case in range(1, T+1):
    # N x M
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            for di, dj in dir:
                dx = i + di
                dy = j + dj
                if 0 <= dx < N and 0 <= dy < M:
                    sum_v += arr[dx][dy]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{test_case} {max_v}')
