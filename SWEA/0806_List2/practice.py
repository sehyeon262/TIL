T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):


