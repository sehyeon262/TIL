V, E = map(int, input().split())

# 인접 행렬 (0, 1로 연결 유무를 모두 저장)
# 7 * 7 의 0 배열 (1 ~ 7 정점 번호를 활용)

def dfs(start_node):
    # q의 의미: 다음에 방문해야 할 노드들 (후보열, 대기열)
    q = [start_node]    # 시작점을 queue에 넣고 시작

    while q:
        # 1. 가장 앞의 노드를 뽑는다
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣는다
        now = q.pop(0)  # O(n) => 웬만하면 쓰지말자
        for next_node in graph[now]:
            # 방문했으면 continue
            if visited[next_node]:
                continue

            visited[next_node] = 1


    # 다음 재귀 호출
    # node로 부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중에서 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지마라!
        if visited[next_node]:
            continue
        
        visited[next_node] = 1
        dfs(next_node)




graph = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1   # => [주의!] 양방향이라면 적어야함!!!

# for row in graph:
#     print(row)

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)    # 양방향인 경우

visited = [0] * (V + 1)     # 방문 여부 기록
visited[1] = 1     # 출발점 초기화
dfs(1)


