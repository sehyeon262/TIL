T = int(input())

for _ in range(1, T+1):
    # A: x에 저장된 값, B: y에 저장된 값
    A, B, N = map(int, input().split())

    cnt = 0
    while max(A, B) <= N:
        if A < B:
            A += B
        else:
            B += A
        cnt += 1
    print(cnt)