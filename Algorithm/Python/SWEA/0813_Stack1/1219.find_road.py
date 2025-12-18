# start: 현재 탐색 중인 정점
# end: 도착점
def DFS(start, end, adjM, visited):
    # 현재 정점이 도착 정점이면 True 반환함
    if start == end:
        return True

    # 현재 정점을 방문했다는 걸 표시함
    visited[start] = True

    # 모든 정점(nv)를 확인함
    for nv in range(len(adjM)):
        # 현재 정점과 연결되어 있고 아직 방문하지 않았다면
        if adjM[start][nv] == 1 and not visited[nv]:
            # DFS로 다음 정점 탐색함
            if DFS(nv, end, adjM, visited):
                # 도착 정점까지 갈 수 있으면 True를 반환!!
                return True
    # 도착 정점에 도달하지 못하면 False 반환!!
    return False


T = 10

for _ in range(1, T + 1):
    # tc : 테스트 케이스 번호, N : 간선 개수
    tc, E = map(int, input().split())
    # 간선 정보를 1차원 리스트로 입력 받음
    edges = list(map(int, input().split()))

    # 정점 개수를 100개라 생각하고 인접 행렬을 만듦
    # 1이면 이동 가능, 0이면 이동 불가능을 표시함
    adjM = [[0] * 100 for _ in range(100)]

    # edges 리스트에서 간선 정보 꺼내서 인접 행렬에 표시함
    # 간선 하나는 시작 정점 -> 끝 정점 두 개의 숫자로 표현 => edges 리스트 길이 = E*2!!!
    # edges 리스트에서 한 번에 2개씩 꺼내기 위해 2씩 반복
    for i in range(0, E * 2, 2):
        x, y = edges[i], edges[i + 1]
        # a에서 b로 가는 길이 있다
        adjM[x][y] = 1

    # 방문 여부 기록하는 리스트 만듦
    visited = [False] * 100

    # 0 ~ 99번 정점까지 갈 수 있는 DFS 탐색함
    if DFS(0, 99, adjM, visited):
        # 갈 수 있음 => 1
        result = 1
    else:
        # 갈 수 없음 => 0
        result = 0

    print(f'#{tc} {result}')