# 중위 순회
def inorder(i):
    global cur
    if i > N:
        return

    else:
        # 완전 이진 탐색이므로 왼쪽 자식의 수는 현재 노드의 2배임
        inorder(i*2)

        # 다음 방문 노드를 위해 cur +1
        T[i] = cur
        cur += 1

        # 완전 이진 탐색 => 오른쪽 탐색은 2배에 +1
        inorder(i * 2 + 1)


T = int(input())
for test_case in range(1, T+1):
    # 노드 개수
    N = int(input())
    # 트리를 배열로 표현한 (인덱스 = 노드 번호)
    T = [0] * (N + 1)

    # 중회순회로 인해 들어갈 값
    cur = 1
    inorder(1)

    print(f'#{test_case} {T[1]} {T[N // 2]}')