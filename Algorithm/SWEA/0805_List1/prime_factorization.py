T = int(input())

# N = 2^a * 3^b * 5^c * 7^d * 11^e
for test_case in range(1, T+1):
    N = int(input())

    # 나머지(%)가 0이면 계속 진행, 아니면 다음으로 넘어감
    # 몫이 1이면 끝남
    a,b,c,d,e = 0,0,0,0,0

    while N > 0:
        if N % 2 == 0:
            a += 1
            N = N // 2
        elif N % 3 == 0:
            b += 1
            N = N // 3
        elif N % 5 == 0:
            c += 1
            N = N // 5
        elif N % 7 == 0:
            d += 1
            N = N // 7
        elif N % 11 == 0:
            e += 1
            N = N // 11
        elif N == 1:
            break
        else:
            pass

    print(f'#{test_case} {a} {b} {c} {d} {e}')





