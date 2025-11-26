T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 흰색: 1, 검은색: 0
    for i in range(N):
        cnt = 0  # 행 흰색(1) 개수
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1

    for i in range(N):
        cnt = 0  # 열 흰색(1) 개수
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1

    print(f'#{test_case} {total}')

