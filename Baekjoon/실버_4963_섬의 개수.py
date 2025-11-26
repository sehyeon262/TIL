# 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
# w와 h는 50보다 작거나 같은 양의 정수이다.
# 1은 땅, 0은 바다이다.
# 한 정사각형과 "가로, 세로 또는 대각선"으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 섬의 개수를 출력
from collections import deque

while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]     # 방문 여부 확인
    cnt = 0     # 섬 개수
    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]   # 위부터 시작해서 시계방향

    # 아직 방문 안 했고, 1이면 => 섬 개수 +1하고 이 땅과 연결된 모든 땅들을 방문 표시함
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    # bfs 함수 실행
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = 1
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # 범위 내이고, 방문하지 않았고, 땅이라면
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

print(cnt)