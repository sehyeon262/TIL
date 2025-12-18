# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

'''
왜 덱을 사용하나?

- 덱은 앞/뒤 양쪽에서 추가할 수 있어서 사용!
- 순간이동(0초)은 더 빠르니까 먼저 탐색 -> 덱 앞(appendleft) 넣기
- 걷기(1초)는 느리니까 나중에 탐색 -> 덱 뒤(append) 넣기
'''

# BFS
from collections import deque

N, K = map(int, input().split())    # N: 수빈 위치, M: 동생 위치
max_d = 100000                      # 최대 위치 범위(0 <= N <= 100000)
dist = [-1] * (max_d + 1)           # 각 위치까지 가는데 걸리는 최소 시간 리스트 (-1: 방문 안 함)
dist[N] = 0                         # 시작 위치는 0초임

dq = deque([N])                     # 탐색할 위치들을 저장함

while dq:
    x = dq.popleft()
    
    # 가지치기 => 동생 찾았으면 종료
    if x == K:
        print(dist[K])  # 그때의 dist[K]가 정답!
        break
    
    # 순간이동 (0초) => 덱 앞에 추가함
    nx = x * 2
    # 범위 안이고 아직 방문 안했다면
    if 0 <= nx <= max_d and dist[nx] == -1:
        dist[nx] = dist[x]  # 0초이므로 시간은 그대로 추가해주면 됨
        dq.appendleft(nx)   # 그리고 덱 앞에 추가하자 -> 우선으로 탐색해야함
        
    # 걷기 (1초) => 덱 뒤에 추가함(나중에 탐색하기 위해서)
    for nx in (x-1, x+1):
        
        if 0 <= nx <= max_d and dist[nx] == -1:
            dist[nx] = dist[x] + 1  # 1초 걸리므로 1 추가
            dq.append(nx)   # 덱 뒤에 추가하자
            

