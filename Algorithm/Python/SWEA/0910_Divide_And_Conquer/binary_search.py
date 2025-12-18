#  B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

def binary_search(A, x):
    left = 0
    right = len(A) - 1
    last = 0    # 직전에 이동한 방향 지정 (이동 전: 0, 왼쪽: -1, 오른쪽: 1)

    while left <=  right:
        m = (left + right) // 2
        if A[m] == x:       # 중앙값이 목표값이면 성공!
            return True
        elif A[m] < x:      # 목표값이 오른쪽 구간에 있을 때
            if last == 1:   # 직전 방향이 1(오른쪽)이었다면 실패!
                return False
            last = 1        # 직전 방향을 오른쪽으로 기록
            left = m + 1    # 구간 좁힘
        else:               # 목표가 왼쪽 구간에 있을 때
            if last == -1:  # 직전 방향이 -1(왼쪽)이었다면 실패!
                 return False
            last = -1       # 직전 방향을 왼쪽으로 기록
            right = m - 1   # 왼쪽으로 구간 좁힘
    return False            # 구간이 소진될 때까지 못 찾으면 실패!

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    ans = 0
    for x in B:
        if binary_search(A, x):
            ans += 1

    print(f'#{test_case} {ans}')
