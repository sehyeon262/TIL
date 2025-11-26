T =int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    cnt = 0  # 빈칸 수
    # 광선이 닿는 곳을 0 -> 1로 바꿔줌
    for i in range(N):
        for j in range(N):
            # 먼저 괴물 찾기
            if arr[i][j] == 2:
                for di, dj in dir:
                    for c in range(1, N):
                        dx = i + di * c
                        dy = j + dj * c
                        # 배열 안의 범위이고 칸이 0일 경우 +1
                        if (0 <= dx < N) and (0 <= dy < N) and (arr[dx][dy] == 0):
                            arr[dx][dy] = 1
                        else:
                            break
    blank_v = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                blank_v += 1
    print(f'#{test_case} {blank_v}')
