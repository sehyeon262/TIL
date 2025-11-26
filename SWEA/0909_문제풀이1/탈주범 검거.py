# 1. BFS로 접근
# - 이동 방향: 상하좌우
# - 이동이 불가능한 케이스
# -- [델타 배열 기본] 범위 밖으로 나가면 못감
# -- [방문 기록 기본] 이미 방문한 곳은 못감
# -- [0이면 못 간다]
# -- [문제 조건]
# --- 현재 내 위치에서 뚫려있는 곳만 이동 가능
# --- 다음 내 위치의 입구가 뚫려 있는 곳으로만 가능
# ----- 이런 케이스들은 델타 배열과 동일한 순서ㅏ(상하좌우)
#           이동 가능 여부를 기록해두면 좋다.

# 2. 방문 기록을 해야한다. (visited)
from collections import deque

# 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라, 이동 가능 여부를 기록
types = {
    # 상하좌우 순서로 기록
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}
# 출발지 행, 열 좌표
def bfs(R, C):
    q = deque([(R, C)])    # 후보군
    visited[R][C] = 1   # 출발점 초기화

    while q: # 후보군이 없을 때까지(더이상 방문할 수 있는 곳이 없으면 종료)
        now_y, now_x = q.popleft() # pop(0)은 비효율적이므로
        dirs = types[graph[now_y][now_x]]

        for dir in range(4):  # 상하좌우 확인
            # 출구가 없으면 다음 방향 확인 (continue)
            if dirs[dir] == 0:
                continue

            # 다음 좌표
            new_y = now_y + dy[dir]
            new_x = now_x + dx[dir]

            # 범위 밖이면 pass
            if new_y < 0 or new_y >= N or new_x <= 0 or new_x >= M:
                continue

            # 못가는 못이면 pass
            if graph[new_y][new_x] == 0:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]

            # 현재 상좌 -> next_dirs가 하우가 안 뚫렸으면 못 간다
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue
            # 현재 하우 -> next_dirs의 상좌가 안 뚫렸으면 못 간다
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            # L 시간 이후는 볼 필요 없다
            if visited[now_y][now_x] + 1 > L:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))


T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는지 기록
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    cnt = 0
    # L 시간 이하로 방문한 모든 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{test_case} {cnt}')
