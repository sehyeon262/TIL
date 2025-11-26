N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        # (r, c)로 올 수 있는 방법이 0이라면 여기서 더 퍼뜨릴 것도 없음
        if dp[r][c] == 0:
            continue

        # 현재 칸에서 점프해야 할 거리
        k = arr[r][c]
        
        # k = 0 이면 이동 불가능한 칸 
        if k == 0:
            continue

        # 아래쪽으로 점프
        nr, nc = r + k, c
        # 범위를 벗어나지 않으면 방법 수를 더해줌
        if nr < N:
            dp[nr][nc] += dp[r][c]

        # 오른쪽으로 점프
        nr, nc = r, c + k
        if nc < N:
            dp[nr][nc] += dp[r][c]

# 도착점에는 모든 경로의 수가 존재함!
print(dp[N-1][N-1])
