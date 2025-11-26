T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 줄(행), M개의 데이터(열)
    picture = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 행 검사
    for i in range(N):
        cnt = 0
        for j in range(M):
            if picture[i][j] == 1:
                cnt += 1
            else:
                # 구조물의 최소 크기는 1x2m 이므로
                if cnt > 1 and max_v < cnt:
                    max_v = cnt
                cnt = 0
        if cnt > 1 and max_v < cnt:
            max_v = cnt

    # 열 검사
    for i in range(M):
        cnt = 0
        for j in range(N):
            if picture[j][i] == 1:
                cnt += 1
            else:
                # 구조물의 최소 크기는 1x2m 이므로
                if cnt > 1 and max_v < cnt:
                    max_v = cnt
                cnt = 0
        if cnt > 1 and max_v < cnt:
            max_v = cnt

    print(f'#{test_case} {max_v}')
