from collections import deque

def find_start():
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                return i, j

def bfs(maze, i, j):
    # visited 생성
    visited = [[0] * 100 for _ in range(100)]
    # 상하좌우
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        if maze[x][y] == '3':
            return 1

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            # 1) 범위 안이고 2) 벽(1)이 아니고 3) 방문하지 않았다면
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] != '1' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
    return 0

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    maze = [list(input()) for _ in range(100)]

    # 시작 변수
    si, sj = find_start()
    result = bfs(maze, si, sj)

    print(f'#{tc} {result}')