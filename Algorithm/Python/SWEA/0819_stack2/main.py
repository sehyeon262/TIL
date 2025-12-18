def f(i , N):
    if i == N:
        print(p)
    else:
        for j in range(1, N):
            P[I], P[J] = P[J]. P[I]
            f(i+1, N)  # i + 1 자리 결정
            p[i], p[j] = p[j], p[i]
