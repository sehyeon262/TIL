T = int(input())

for test_case in range(1, T+1):
    numbers = int(input())
    lst = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

    for i in range(6):
        lst[numbers % 10] += 1 # 각 숫자에 맞는 인덱스에 +1 (나머지 이용)
        numbers //= 10

    i = 0
    # tri: 연속되는 숫자, run: 똑같은 숫자
    tri = run1 = 0 # 횟수
    while i < 10:
        # triplete 조사 후 데이터 삭제
        if lst[i] >= 3:
            lst[i] -= 3
            tri += 1
            continue

        # run 조사 후 데이터 삭제
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            lst[i] -= 1
            lst[i+1] -= 1
            lst[i+2] -= 1
            run1 += 1
            continue

        i += 1  # tri와 run이 더이상 존재하지 않으면 i를 1 증가

    if run1 + tri == 2:
        print(f'#{test_case} Baby Gin')

    else:
        print(f'#{test_case} Lose')
