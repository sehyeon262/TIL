from collections import deque

# 전체 보드를 훑어서 값이 2인 좌표 찾음
def find_start(N):
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                return i, j

def bfs(si, sj, N):
    # 초기화
    # visited 생성 => 0: 방문 안 함, 그 외의 양수: 시작점에서의 거리
    visited = [[0] * N for _ in range(N)]

    q = deque()
    # 큐에는 좌표를 넣음
    q.append((si, sj))
    # 시작칸의 거리를 1로 시작 (마지막에 -2 하면 됨)
    visited[si][sj] = 1
    # 상 하 좌 우
    dir = [[-1,0], [1,0], [0,-1], [0,1]]

    # 큐(q)가 빌 때까지 반복
    while q:
        # 디큐 => 현재 칸
        ti, tj = q.popleft()
        # 현재 칸이 도착점이 3이면, 방문거리 - 2
        if miro[ti][tj] == 3:
            return visited[ti][tj] - 2

        for di, dj in dir:
            wi, wj = ti + di, tj + dj
            # 1) 범위 안이고 2) 벽(1)이 아니고 3) 아직 방문 안 했으면 이동
            if 0 <= wi < N and 0 <= wj < N and miro[wi][wj] != 1 and visited[wi][wj] == 0:
                # 거리 갱신(한 칸 더 이동했으므로 +1)
                visited[wi][wj] = visited[ti][tj] + 1
                q.append([wi,wj])
    # 여기까지 왔다면 도착을 찾지 못 한 것 => 0 반환
    return 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{test_case} {ans}')

