# 이진 최소힙
# 부모 노드의 값 < 자식 노드의 값
# 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
#  N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고,
#  마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    for i in node:
        last += 1
        idx = last
        heap[idx] = i
        # 부모보다 작으면 위로 올림
        while idx > 1 and heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx //= 2   # 루트까지 검사

    sum_v = 0
    i = last
    while i > 1:
        i //= 2
        sum_v += heap[i]

    print(f'#{test_case} {sum_v}')