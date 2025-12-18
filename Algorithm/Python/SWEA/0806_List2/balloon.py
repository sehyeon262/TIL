T = int(input())

for test_case in range(1, T + 1):
    # N: 행(세로)의 수, M: 열(가로) 수
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상, 우, 하 ,좌 (시계방향)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    max_v = 0
    for i in range(N):  # 행
        for j in range(M):  # 열
            # 현재 위치의 값부터 합산 시작
            s = arr[i][j]
            # 4가지 방향 각각에 대해 계산함
            for d in range(4):
                nx = i + dx[d]  # 행 인덱스
                ny = j + dy[d]  # 열 인덱스
                if 0 <= nx < N and 0 <= ny < M:
                    s += arr[nx][ny]
            if max_v < s:
                max_v = s

    print(f'#{test_case} {max_v}')

