from heapq import heappop, heappush

T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))


    INF = float('inf')
    weight = [INF] * (N + 1)    # 시작점에서 각 정점까지의 최단거리 배열
    pq = [(0, 0)]               # 우선순위 큐에 (현재까지 거리, 정점) 형태로 저장
    weight[0] = 0               # 시작점까지의 거리는 0으로 초기화

    while pq:
        cur_weight, loc = heappop(pq)   # 현재까지 거리가 가장 작은 정점을 꺼냄
        # 이미 더 짧은 거리로 방문한 적이 있으면 스킵함 
        if weight[loc] < cur_weight:
            continue

        for next_loc, margin_weight in graph[loc]:
            next_weight = cur_weight + margin_weight
            # 더 짧은 경로를 찾으면 갱신하고 우선순위 큐에 넣어 다음에 처리
            if next_weight < weight[next_loc]:
                weight[next_loc] = next_weight
                heappush(pq, (next_weight, next_loc))
    
    print(f'#{test_case} {weight[N]}')
        