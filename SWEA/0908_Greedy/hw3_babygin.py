def game(lst, x):
    # run => 숫자 연속 3개 이상
    if lst[x] >= 1 and lst[x+1] >= 1 and lst[x+2] >= 1:
        return True

    # triplet => 같은 숫자 3개 이상
    if lst[x] >= 3:
        return True
    return False    # 둘 다 아니면 False


T = int(input())
for test_case in range(1, T+1):
    cards = map(int, input().split())
    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0

    # 카드 가져가기
    for i, x in enumerate(cards):
        if i % 2 == 0:
            p1[x] += 1
            if game(p1, x):
                ans = 1
                break
        else:
            p2[x] += 1
            if game(p2, x):
                ans = 2
                break

    print(f'#{test_case} {ans}')

