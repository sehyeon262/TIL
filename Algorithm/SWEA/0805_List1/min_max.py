T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 양수의 개수
    ai = list(map(int, input().split()))  # N개의 양수

    # 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 => abs 사용
    # 단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고,
    # 큰 수가 여러 개이면 마지막으로 나오는 위치로 함.

    # 큰 값과 작은 값의 인덱스를 각각 구함
    min_num = ai[0]
    max_num = ai[0]
    min_idx = 1
    max_idx = 1
    for i in range(len(ai)):
        if max_num <= ai[i]:  # max_num과 같거나 큰 값이면 최대값으로 선택
            max_idx = i + 1
            max_num = ai[i]

        if min_num <= ai[i]:  # min_num보다 크거나 같으면 continue
            continue
        else:  # min_num보다 작으면 최소값으로 선택
            min_idx = i + 1
            min_num = ai[i]


    # 구한 후 abs(최대값 - 최소값) 출력
    result = abs(max_idx - min_idx)
    print(f'#{test_case} {result}')
