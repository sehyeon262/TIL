# 방향성이 없는 그래프가 주어진다. 
# 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 임의로 주어진 두 정점은 반드시 통과해야 한다는 것
# 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 
# 다익스트라

import sys, heapq
input = sys.stdin.readline
INF = int(1e15)


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    # start에서 각 정점까지의 최단 거리 저장할 배열임
    dist = [INF] * (N + 1)

    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 정점)

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dist[cur_node]:
            continue
        
        # 현재 정점과 연결된 다른 정점 확인
        for next_node, cost in graph[cur_node]:
            # 현재 거리 + 간선 비용
            new_dist = cur_dist + cost

            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return dist

dist1 = dijkstra(1)     # 1에서 시작
dist2 = dijkstra(v1)    # v1에서 시작
dist3 = dijkstra(v2)    # v2에서 시작

'''
2가지 경우 있음!
=> 1 → v1 → v2 → N
=> 1 → v2 → v1 → N
'''

path1 = (dist1[v1] + dist2[v2] + dist3[N])
path2 = (dist1[v2] + dist3[v1] + dist2[N])

res = min(path1, path2)

print(res if res < INF else -1)