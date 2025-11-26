# 물을 큐에 다 넣는다
# q가 비어있지 않을 때까지 반복
# 하나씩 pop 하면서 인접 리스트에 자기자신값 + 1 을 더하고 큐에 넣음
# visited 방문 표시
# 만약 방문했다면 pass
from collections import deque

# 물을 찾아서 큐에 다 넣음
def find_water():
    for i in range(N):
        for j in range(M):
            if map[i][j] == 'W':
                queue.append([i,j])
    return queue

def bfs(q):
    q = deque()
    # 방문 표시 리스트
    visited = [[0] * M for _ in range(N)]
    # 상 하 좌 우
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = q.popleft()
    visited[x][y] = 1

    while q:
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            # 1) 범위 안이고 2)방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] =  1
                map[nx][ny] = map[nx][ny] + 1
                q.append([nx, ny])

    sum_v = 0
    for i in range(N):
        for j in range(M):
            sum_v += map[i][j]

    return sum_v



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    map = [list(input()) for _ in range(N)]



    result = bfs(q)

    print(f'#{test_case} {result}')