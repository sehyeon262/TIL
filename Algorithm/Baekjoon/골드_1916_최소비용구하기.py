# N개의 도시 있음
# 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스 있음
# A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 함.
# 최소비용 출력해라.
# 도시의 번호는 1 ~ N 까지다.

from heapq import heappop, heappush 

N = int(input())   # 도시 개수(1 <= N <= 1,000)
M = int(input())   # 버스 개수(1 <= M <= 100,000)
graph = [[] for _ in range(N+1)]
# graph[x] → x번 도시에서 출발하는 버스 목록 저장

# 버스 정보 :
# 출발 도시 번호, 도착지 도시 번호, 그 버스 비용(0 <= w <= 100,000)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 출발 도시번호, 도착 도시번호
s, e = map(int, input().split())

def dijkstra(start):
    dist = [float('inf')] * (N+1)   # 각 정점까지의 최단거리 저장할 리스트
    dist[start] = 0     # 시작 노드 최단거리는 0
    
    pq = []
    heappush(pq, (0, start))

    while pq:
        cost, cur = heappop(pq)

        if dist[cur] < cost:
            continue

        for nxt, w in graph[cur]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heappush(pq, (new_cost, nxt))

    return dist

result = dijkstra(s)
print(result[e])       