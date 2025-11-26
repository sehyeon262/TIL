T = int(input())


for test_case in range(1,T+1):
    counts = [0] * 10  # 카운트 배열
    N = int(input())
    ai = list(map(int, list(input())))

    for i in range(len(ai)):
        counts[ai[i]] += 1

    max_num = max(counts)  # 가장 많은 카드의 장 수
    max_card = 0
    for j in range(len(counts)):
        if max_num == counts[j]:
            max_card = j  # 가장 많은 카드의 숫자

    print(f'#{test_case} {max_card} {max_num}')


