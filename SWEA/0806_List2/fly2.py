T = int(input())

for test_case in range(1, T+1):
    # N: 배열, M: 분사되는 칸 수
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # '+' 또는 'X'로 분사함
    # 한 번만 뿌려 최대한 많은 파리를 잡으려고 함

    max_v = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]  # i, j를 중심으로
            for di, dj in [[]]

