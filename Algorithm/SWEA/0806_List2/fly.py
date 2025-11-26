T = int(input())

for test_case in range(1, T+1):
    # N: 전체 배열 크기, M: 부분 배열 크기
    N, M = map(int, input().split())
    # N x N 배열 만들기
    N_arr = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        N_arr.append(arr)

    max_fly = 0
    for i in range(N - M + 1):  # 파리채 왼쪽 위 모서리가 올 수 있는 행 번호
        for j in range(N - M + 1):  # 파리채 왼쪽 위 모서리가 올 수 있는 열 번호
            fly_sum = 0
            # M x M 탐색
            # M x M 파리채 영역 안을 하나씩 돌면서 그 안에 있는 파리 수 모두 더함
            for x in range(M):  # 파리채 행
                for y in range(M):  # 파리채 열
                    fly_sum += N_arr[i + x][j + y]
            if fly_sum > max_fly:  # 지금 잡은 파리 수가 가장 많으면
                max_fly = fly_sum  # 최고 기록 저장

    print(f'#{test_case} {max_fly}')

