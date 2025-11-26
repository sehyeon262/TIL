T = int(input())

for test_case in range(1, T+1):
    # N x M 배열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 8방향 이동 좌표 (왼쪽 위 대각선부터 시계방향)
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    result = 0  # 예비 후보지 수
    # 모든 좌표에 대해 검사
    for i in range(N):
        for j in range(M):
            cnt = 0  # 현재 칸 보다 낮은 칸의 개수
            # 8방향 검사
            for dir in range(8):
                nx = i + dx[dir]
                ny = j + dy[dir]
                # 현재칸보다 값이 작고, 범위를 벗어나지 않았으면 +1
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] < arr[i][j]:
                    cnt += 1
            # 낮은 지역이 4곳 이상이면 후보지임
            if cnt >= 4:
                result += 1
    print(f'#{test_case} {result}')
