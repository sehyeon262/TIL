from collections import deque

# N: 동기 수, M: 친구 관계 수
N = int(input())
M = int(input())

# 인접 리스트 
graph = [[] for _ in range(n + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 친구 관계는 양방향이므로 둘 다 추가함
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부와 거리를 함께 기록할 리스트
# 0으로 초기화, 방문 시 거리(depth)를 저장
visited = [0] * (N + 1)

q = deque()

# 1. 시작점 처리
q.append(1)  # 큐에 상근이(1)를 넣음
visited[1] = 1 # 상근이는 방문했다고 표시 (거리는 중요하지 않음)
invite_count = 0 # 초대할 사람 수

# 2. BFS 탐색 시작
while q:
    now = q.popleft() # 큐에서 한 명을 꺼냄

    # 친구(거리 1) 또는 친구의 친구(거리 2)까지만 초대
    # 현재 위치(now)의 거리가 3이면 더 이상 탐색하지 않음
    if visited[now] >= 3:
        continue
    
    # 현재 위치(now)와 연결된 친구들을 확인
    for friend in graph[now]:
        # 아직 방문하지 않은 사람이라면
        if visited[friend] == 0:
            # 초대 명단에 추가
            invite_count += 1
            # 방문 처리 (현재 위치까지의 거리 + 1)
            visited[friend] = visited[now] + 1
            # 다음 탐색을 위해 큐에 추가
            q.append(friend)

# 3. 결과 출력
print(invite_count)