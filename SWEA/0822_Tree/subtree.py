T = int(input())

# 노드 번호는 1 ~ E + 1번까지존재
for test_case in range(1, T+1):
    # E: 간선 개수
    # N을 루트로 하는 서브 트리에 속한 노드 개수 알아내기
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    # 인덱스를 0 ~ E + 1을 사용하므로 E + 2로 길이 조정
    # 각 부모 p의 첫째 자식
    c1 = [0] * (E + 2)
    # 각 부모 p의 둘째 자식
    c2 = [0] * (E + 2)

    # 두개씩 값을 받으면서 부모, 자식에 값 넣음
    for i in range(0, E*2, 2):
        p, c = node[i], node[i+1]
        # 첫째 자식이 없으면 할당
        if c1[p] == 0:
            c1[p] = c
        # 첫째 자식 있을 경우, 둘째 자식에 할당
        else:
            c2[p] = c

    # 서브트리 개수
    cnt = 0
    # 방문 시작할 처음 노드 스택에 넣고 시작함
    stack = [N]
    # 스택이 빌 때까지 반복
    while stack:
        x = stack.pop()
        # 자식이 없을 때 0이 들어오므로 건너뜀
        if x == 0:
            continue
        cnt += 1

        # 자식이 존재하면 스택에 넣음 => 또 그 다음 자식을 찾기 위해
        if c1[x]:
            stack.append(c1[x])
        if c2[x]:
            stack.append(c2[x])

    print(f'#{test_case} {cnt}')
