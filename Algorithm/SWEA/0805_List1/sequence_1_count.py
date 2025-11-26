T = int(input())

for test_case in range(1, T+1):
    N =int(input())  # 수열의 길이
    sequence = list(map(int,list(input())))  # N개의 0,1로 구성된 수열

    count = 0 # 연속한 1의 개수
    max_count = 0 # 최대 연속 1의 개수
    for i in range(len(sequence)):
        if sequence[i] % 2 == 1: # 1이 나오면 count에 추가
            count += 1
        else:  # 0이 나오면
            # 현재 1의 개수가 최대 연속 1의 개수보다 크면 최대값으로 설정
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count

    print(f'#{test_case} {max_count}')
