def bfs(s, V):
    # 초기화
    visited = [0] * (V + 1)  # visited 생성
    q = [s]   # 큐 생성
                # 시작점 인큐
    visited[s] = 1   # 시작점 인큐 표시

    # 반복
    while q:    # 탐색할 정점이 남아 있으면
        t = q.pop(0)    # 디큐 (앞에서 꺼내는 거이므로)
        print(t)        # visit(),방문정점 출력
        for w in adj_lst[t]:        # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

