T = int(input())
# N은 1 이상 30 이하의 정수

for test_case in range(1, T+1):
    N = int(input())  # 행 개수
    arr = list([0] * N for _ in range(N)) # 크기에 맞는 배열 만듦(N x N)

    # 오른쪽 -> 아래 -> 왼쪽 -> 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    way = 0  # 초기 방향

    # 시작 좌표
    x, y =0, 0
    for num in range(1, N*N+1):
        # 숫자 채우기
        arr[x][y] = num

        nx = x + dx[way]
        ny = y + dy[way]

        # 배열 범위 밖이거나
        # 다음 칸이 채워져 있으면(0이 아닌거)
        # 배열 이동
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            if way == 0:
                way = 1  # 아래
            elif way == 1:
                way = 2  # 왼쪽
            elif way == 2:
                way = 3  # 위
            else:
                way = 0  # 오른쪽

            # 방향 전환 후 위치 다시 계산
            nx = x + dx[way]
            ny = y + dy[way]

        # 다음 위치로 이동
        x, y = nx, ny

    print(f"#{test_case}")
    for row in arr:
        print(*row)
