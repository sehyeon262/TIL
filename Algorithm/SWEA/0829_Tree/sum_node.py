T = int(input())

for test_case in range(1, T+1):
    # 노드 개수, 리프노드 개수, 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        # 노드 번호, 저장된 값
        num, val = map(int, input().split())
        tree[num] = val

    # 아래에서 위로 올라가며 자식이 있으면 더해줌
    # 마지막 레벨은 오른쪽 자식이 없을 수 있으므로 경계 체크 해줘야함!!
    for i in range(N, 0, -1):
        left = i * 2
        right = i * 2 + 1
        # 왼쪽 자식이 존재하면 더함
        if left <= N:
            tree[i] += tree[left]
        # 오른쪽 자식이 존재하면 더함
        if right <= N:
            tree[i] += tree[right]

    print(f'#{test_case} {tree[L]}')


