T = int(input())

# si, sj : 시작점 좌표
def DFS(si, sj):

    # 중복체크 배열도 2차원
    visited = [[0] * N for _ in range(N)]
    # [x, y]를 탐색한 적인 있다. => visited[x][y] = 1
    # [w, z]를 탐색한 적이 없다. => visited[x][y] = 0

    # 왔던길로 되돌아가기 위한 스택
    stack = []

    # 현재 탐색중인 위치
    vi, vj = si, sj

    # 시작지점 방문 체크
    visited[vi][vj] = 1

    # 델타 방법
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 탐색 시작
    while True:
        # 현재 위치 vi, vj에서 탐색
        # 현재 위치가 도착점인가? 검색
        if maze[vi][vj] == 3:
            # 도착점에 왔으면 더이상 진행 할 필요 없은
            return 1
        # (vi, vj)에서 갈 수 있는 다른 위치 찾기
        # (ni, nj) : 다른 위치
        # 4방향
        for d in range(4):
            # d 방향으로 갔을 때 다른 위치 ni, nj 구하기
            ni = vi + di[d]
            nj = vj + dj[d]

            # 1. ni, nj가 2차원 배열 안인지
            # 2. 실제로 갈 수 있다고 표시된 곳인지 (벽 == 1, 길 == 0)
            # 3. 이전에 방문한 적 없는 지
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1) and (not visited[ni][nj]):
                # (ni, nj)로 이동할 것이기 때문에 현재 위치(vi, vj)를 스택에 저장
                stack.append((vi, vj))
                visited[ni][nj] = 1
                vi, vj = ni, nj
                # 내가 가려는 방향 정했으면 다른 방향 전혀 안 봐도 됨
                break

        # 끝까지 갔는데 없음 => 돌아오고싶음 => 스택이 알고있음
        else:
            # 중간에 break 한 적이 없다 => 갈 수 있는 방향이 없다.
            # 길이 없다는 거니깐 돌아가자
            # 어디로 돌아가는데? => 스택이 알고있다
            if stack:
                # 길이가 2인 튜플 나옴 => 변수 2개 준비하면 알아서 쪼개줌
                vi, vj = stack.pop()
            else:
                break
    # 탐색을 다 마쳤는데 3을 발견 못하면 return 0
    return 0



for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())

    # 미로
    maze = [list(map(int, input())) for _ in range(N)]

    # 탐색 시작 좌표
    # si, sj
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                # 시작점
                si, sj = i, j

    print(f'#{tc} {DFS(si, sj)}')
