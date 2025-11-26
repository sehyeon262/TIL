import sys
sys.stdin = open('sample_input.txt',  'r')
# sys.stdout = open('output.txt', 'w')

# 배열 크기 100 x 100
# 각 행의 합은 정수 범위 넘지 않음
# 동일한 최댓값이 있을 경우, 하나의 값만 출력
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값 구하라!!!!

T = 10
for test_case in range(1,T+1):
    tc = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]
    total_lst = []

    # 각 행의 합 구하기
    max_row = 0
    for i in range(100):
        r_count = 0
        for j in range(100):
            r_count += arr[i][j]
        if max_row < r_count:  # 행들 중 가장 큰 값 구함
            max_row = r_count
    total_lst.append(max_row)

    # 각 열의 합 구하기
    max_col = 0
    for i in range(100):
        c_count = 0
        for j in range(100):
            c_count += arr[j][i]
        if max_col < c_count:
            max_col = c_count
    total_lst.append(max_col)

    # 오른쪽 밑으로 가는 대각선의 합 구하기
    r_count = 0
    for i in range(100):
        r_count += arr[i][i]
    total_lst.append(r_count)

    # 왼쪽 밑으로 가는 대각선의 합 구하기
    l_count = 0
    for i in range(100):
        l_count += arr[99-i][i]
    total_lst.append(l_count)

    # result = max(total_lst)

    # total_lst 버블정렬
    for i in range(len(total_lst)-1, 0, -1):
        for j in range(i):
            if total_lst[j] > total_lst[j+1]:
                total_lst[j], total_lst[j+1] = total_lst[j+1], total_lst[j]
    result = total_lst[-1]

    print(f'#{test_case} {result}')