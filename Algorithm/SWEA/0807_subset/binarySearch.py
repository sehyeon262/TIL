
T = int(input())

def binary_search(pages, target):  # a: 배열
    start = 1
    end = pages
    count = 0  # 몇 번만에 찾았는지 세는 변수
    while start <= end:
        count += 1
        middle = (start + end) // 2
        if middle == target:
            return count
        elif middle > target:  # 찾는 값보다 크면
            end = middle  # 왼쪽 구간 선택
        else:  # 찾는 값보다 작으면
            start = middle  # 오른쪽 구간 선택


for test_case in range(1, T+1):
    # P: 전체 쪽 수, A: A가 찾을 쪽 번호, B: B가 찾을 쪽 번호
    P, A, B = map(int, input().split())

    PA = binary_search(P, A)
    PB = binary_search(P, B)

    if PA < PB:
        result = 'A'
    elif PA > PB:
        result = 'B'
    else:
        result = '0'
    print(f'#{test_case} {result}')
