T = int(input())

for test_case in range(1, T+1):
    # N: 숫자 개수, M: 작업 횟수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    cq = [0] * N
    rear = 0

    # 원소 삽입
    for i in range(N):
        cq[rear + i] = nums[i]

    # 이동 작업
    for i in range(M):
        start = nums[(i+1) % N]

    print(f'#{test_case} {start}')


