T = int(input())

# 그래프가 주어집니다. (노드와 간선 정보)
# 두 노드가 경로로 연결되어 있으면 1, 아니면 0을 출력하세요.
# 예를 들어, 1번 노드에서 6번 노드로 가는 경로가 있으면 1을 출력합니다.

# E개의 간선 정보가 주어집니다. (어떤 노드와 어떤 노드가 연결되어 있는지)
# 마지막에 출발 노드와 도착 노드가 주어집니다.
# 출발 노드에서 도착 노드로 갈 수 있으면 1, 없으면 0을 출력

for test_case in range(1, T+1):
    # 노드(정점) 수: V, 간선 수: E
    V, E = map(int, input().split())

    # 연결 정보를 인접행렬? 인접리스트?
    # 인접 행렬 사용시
    adjm = [[0] * (V+1) for _ in range(V+1)]

    # 간선 정보가 E개
    for i in range(E):
        # s에서 e로 가는 길이 있다, 역방향은 없음(유향그래프)
        s, e = map(int, input().split())

        adjm[s][e] = 1

    # 출발 정점 S와 목표 정점 G
    S, G = map(int, input().split())

    # 문제에서 원하는 답: S에서 출발해서 G로 갈 수 있는가?
    # 일단 못간다 라고 가정하고 참색중에 G를 만나면 가능하다고 고칠 것이다.
    answer = 0

    # DFS
    # 이전에 방문한 적 있는지 체크를 위한 방문 배열
    visited = [0] * (V+1)
    # 스택
    stack = []

    # 시작지점은 방문했다고 처리
    # 현재 위치를 v라고 했을 때 S에서 탐색 시작
    v = S
    visited[S] = 1

    while True:

        # 현재 위치가 도착지점 G인가?
        if v == G:
            # S에서 G로 가는 길 발견
            answer = 1
            break

        # 현재 정점 v에서 방문 가능한 다음 정점 nv를 참색
        for nv in range(1, V+1):
            # nv 정점이 v와 인접해있고 이전에 방문한 적 없어야 갈 수 있다.
            if adjm[v][nv] == 1 and visited[nv] == 0:
                # nv 정점은 갈 수 있다
                # 현재 위치 v를 스택에 저장
                stack.append(v)
                # nv는 방문 했다라고 표시
                visited[nv] = 1
                # nv로 이동
                # 현재위치 v를 nv로 변경
                v = nv
                # 이동했으므로 다른 정점 탐색 x
                break
        else:
            # 갈 수 있는 정점 nv를 발견하지 못한 경우
            # 스택에서 돌아갈 위치를 하나 꺼내서 현재 위치를 변경
            # 스택이 비어있는지 확인
            if stack:
                v = stack.pop()
            # 스택이 비어있으면
            else:
                # 갈 수 있는 곳도, 돌아갈 곳도 없음 -> 탐색 종료
                break

    print(f'#{test_case} {answer}')