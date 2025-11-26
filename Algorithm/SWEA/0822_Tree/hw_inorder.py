T = 10

for test_case in range(1, T+1):
    # N : 정점의 총 수
    N = int(input())

    # 노드 문자/ 왼쪽/ 오른쪽 자식 번호를 담을 배열
    val = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        nodes = input().split()
        # 입력의 첫 번째 원소는 정점 번호에 해당
        idx = int(nodes[0])
        # 이 정점에 해당하는 문자 (한 글자)
        val[idx] = nodes[1]

        # 자식 정보는 있을 수도/ 없을 수도 있으니 3개 이상 있으면 자식이 있는 거임
        if len(nodes) >= 3:
            left[idx] = int(nodes[2])
        if len(nodes) >= 4:
            right[idx] = int(nodes[3])

    # 방문한 문자들을 차례대로 담을 리스트
    ans = []
    # 중위순회 => 좌 -> 노드 -> 우
    def inorder(i):
        # 자식이 없음을 0으로 표현했으므로 0이면 바로 리턴 반환
        if i == 0:
            return
        # 왼쪽 서브트리 먼저 전부 방문
        inorder(left[i])
        # (젤 마지막에 방문한) 현재 노드의 문자 기록
        ans.append(val[i])
        # 마지막으로 오른쪽 서브트리 방문
        inorder(right[i])

    # 루트 노드는 항상 1이라고 문제에서 보장함
    inorder(1)

    print(f"#{test_case} {''.join(ans)}")