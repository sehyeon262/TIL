from collections import deque

T = int(input())
for test_case in range(1, T+1):
    # V: 정점 개수, E: 간선 개수
    V, E = map(int, input().split())
    # 그래프를 "인접 리스트"로 저장함
    # 노드가 1부터 시작하므로 크기를 V + 1로 만듦
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        # 간선의 양쪽 노드 번호
        a, b = map(int, input().split())
        # 무방향!!!!이므로 양쪽으로 갈 수 있음
        graph[a].append(b)
        graph[b].append(a)

    # S: 출발 노드, G: 도착 노드
    S, G = map(int, input().split())

    # visited[i] => S(출발)에서 i까지의 '간선 개수'
    # 0이면 방문하지 않은 상태임
    visited = [0] * (V+1)

    q = deque([S])
    visited[S] = 0

    while q:
        # 가장 먼저 들어온 정점 꺼냄
        x = q.popleft()
        # BFS는 처음 목표노드에 도착했을 때 거리가 최단이므로 종료함
        if x == G:
            break

        for y in graph[x]:
            # 아직 방문하지 않은 정점만 방문함
            if visited[y] == 0:
                # S -> x까지의 거리 + 1 => S -> y까지의 거리
                visited[y] = visited[x] + 1
                # 다음 탐색 대상으로 큐에 추가함
                q.append(y)

    result = 0 if visited[G] == 0 else visited[G]

    print(f'#{test_case} {result}')

