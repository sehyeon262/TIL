import heapq
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))

def dijkstra(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if dist[cur] < cur_dist:
            continue

        for nxt, cost in graph[cur]:
            new_dist = cur_dist + cost
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    return dist

# X -> 모든 마을
dist_from_X = dijkstra(X, graph)

# 모든 마을 -> X (역방향 그래프)
dist_to_X = dijkstra(X, reverse_graph)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, dist_from_X[i] + dist_to_X[i])

print(answer)

