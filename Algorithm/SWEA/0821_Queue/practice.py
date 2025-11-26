from collections import deque

def bfs(graph, S):
    # visited 생성
    visited = [0] * len(graph) + 1
    # 큐 생성
    q = deque()
    # 시작점 인큐
    q.append(S)
    # 시작점 방문 표시
    visited[S] = 1

    while q:
        # 디큐
        a = q.popleft()
        # 방문해서 할 일 처리
        for i in graph[a]:
            if visited[i] != 0:
                q.append(i)
                visited[a] = 1


