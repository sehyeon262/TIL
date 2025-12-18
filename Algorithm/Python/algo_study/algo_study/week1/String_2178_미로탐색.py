N, M = map(int, input().split())
# N x M
arr = [list(input()) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 좌표
x, y = 0, 0
# 이동 칸 수 => 시작 위치부터 셈
cnt = 1

# 방문 했다면 True, 방문 안 했다면 False
visited = [[False] * M for _ in range(N)]
visited[x][y] = True

# 도착 지점인 (N-1, M-1)에 도착하기 전까지 반복함
while (x, y) != (N-1, M-1):
    moved = False
    for i in range(4):
        nx = x + dx[i]  # 행
        ny = y + dy[i]  # 열

        # 미로 범위 안인가?
        if 0 <= nx < N and 0 <= ny < M:
            # 갈 수 있는 길(1)인지?
            if arr[nx][ny] == '1' and not visited[nx][ny]:
                x, y = nx, ny
                visited[x][y] = True
                cnt += 1
                moved = True
                break  # 한 방향으로 이동했으니 break
    
    if not moved:
        break

print(cnt)
