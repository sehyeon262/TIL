T = int(input())

# 상 하 좌 우 (이동 방향)
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def DFS(x, y):
    # 현재 위치가 목적지(3)라면 True 반환함
    if maze[x][y] == 3:
        return True

    # 방문 표시하기
    visited[x][y] = 1

    # 상, 하, 좌, 우 네 방향으로 탐색함
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        # 1) 범위 안에 있는가?
        # 2) 벽(1)이 아닌가?
        # 3) 방문 안 한 곳인가?
        if (0 <= nx < N) and (0 <= ny < N) and (maze[nx][ny] != 1) and (not visited[nx][ny]):
            # 다음 경로에서 도착 가능하면 True
            if DFS(nx, ny):
                return True

    return False

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 한 번 방문한 곳은 다시 가지 않도록 방문 배열 사용 (0: 방문 안 함, 1: 방문함)
    visited = [[0] * N for _ in range(N)]

    # 시작 위치 찾기 (2가 있는 좌표)
    start_x, start_y = -1, -1
    for i in range(N):
        for j in range(N):
            # 시작점을 발견했으면?
            if maze[i][j] == 2:
                start_x, start_y = i, j
                break

    # DFS 탐색 결과에 따라 1(성공) 또는 0(실패) 출력
    result = 1 if DFS(start_x, start_y) else 0
    print(f'#{test_case} {result}')
