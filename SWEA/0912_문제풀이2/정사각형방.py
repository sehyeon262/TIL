# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 물론 이동하려는 방이 존재해야 하고, 
# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

# DFS => 터짐
# BFS => 가능 

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)     # 1번 ~ N^2 번 방 번호
    
    # 현재 위치 숫자 기준 상하좌우를 확인
    # -> 1 큰게 있으면 visited에 1이라고 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 밖 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동 가능합니다!
                    visited[arr[y][x]] = 1
                    break   # 다른 방향 볼 필요 없다
    # print()

    # 연속된 1의 개수가 가장 긴 곳을 찾는다.
    max_cnt = 0 # 정답
    cnt = 0     # 하나하나마다 몇 개가 연속되는지?
    start = 0   # 숫자를 세기 시작한 위치
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:   # 0을 만나면 계산
            if max_cnt < cnt:
                max_cnt = cnt   # 최대값 갱신
                start = i - cnt # 시작점 찾기
            cnt = 0 # 개수 초기화
    print(f'#{test_case} {start} {max_cnt + 1}')


# ------- 내가 연습한 코드 --------

# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 
# 이 숫자는 모든 방에 대해 서로 다르다.
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다. => 4방향 지정
# 물론 이동하려는 방이 존재해야 하고, => 범위 설정
# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# "처음에 어떤 수가 적힌 방에서 있어야" 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성
# => "처음에 출발해야 하는 방 번호"와 "최대 몇 개의 방을 이동할 수 있는지"를 공백으로 구분하여 출력
# => 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 "그 중에서 적힌 수가 가장 작은 것"을 출력한다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우

    for x in range(N):
        for y in range(N):
            for i, j in dir:
                nx = x + i
                ny = y + i
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                if grid[nx][ny] == grid[nx][ny] + 1:
                    visited[grid[nx][ny]] = 1
