import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동 정의
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

time = 0        # 총 걸린 시간(=라운드 수)
last = 0        # 마지막에 녹은 치즈 개수

while True:
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    melt_list = []  # 이번 시간에 녹일 치즈들 저장

    # 1. 바깥 공기 BFS
    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            # 범위 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue

            # 아직 안 간 곳이면
            if board[nx][ny] == 0:
                # 공기면 그냥 계속 확장
                visited[nx][ny] = True
                q.append((nx, ny))

            elif board[nx][ny] == 1:
                # 치즈면 지금은 못 들어가지만, 외부 공기에 닿았으므로 녹일 대상
                visited[nx][ny] = True
                melt_list.append((nx, ny))

    # 2. 더 녹을 치즈가 없으면(= 이미 전부 녹음) 종료
    if not melt_list:
        break

    # 3. 치즈 녹이기
    last = len(melt_list)  # 이번에 녹은 치즈 개수
    for x, y in melt_list:
        board[x][y] = 0    # 녹아서 공기가 됨

    time += 1  # 한 시간 경과

# 결과 출력
print(time)
print(last)
