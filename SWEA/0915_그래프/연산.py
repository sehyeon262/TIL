# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지
# 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램
from collections import deque

def bfs(N):
    
    while q:
        x, cnt = q.popleft()
        
        if x == M:          # 목표 숫자 M에 도달하면
            return cnt      # 지금까지의 연산 횟수 반환 

        for nx in (x-1, x+1, x*2, x-10):
            # M의 범위 안이고 방문하지 않았다면
            if 1 <= nx < limit and not visited[nx]:
                visited[nx] = 1             # 방문처리
                q.append((nx, cnt + 1))     # 큐에 (다음 숫자, 연산횟수 + 1)을 넣음


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    q = deque()         # 큐 생성
    q.append((N, 0))    # (시작값 N, 횟수 0) 넣고 시작
    limit = 1000001
    visited = [0] * limit   
    visited[N] = 1      # 시작 숫자 방문 처리
    res = bfs(N)
    print(f'#{test_case} {res}')