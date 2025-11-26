T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 수열의 길이
    seq = list(map(int, list(input())))  # N개의 수열

    sum_seq = 0
    one_v = 0
    for i in range(N):
        if seq[i] == 1:
            one_v += 1
        else:
            if sum_seq < one_v:
                sum_seq = one_v
            one_v = 0
        if sum_seq < one_v:
            sum_seq = one_v
    print(f'#{test_case} {sum_seq}')


