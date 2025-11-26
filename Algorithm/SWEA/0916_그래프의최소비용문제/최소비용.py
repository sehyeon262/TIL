# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에,
# 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.
# 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래
# 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

# (N-1, N-1) 이면 종료!

from heapq import heappop, heappush

def prim(x, y):
    pq = [(0, 0)]   # 시작 위치를 큐에 넣고 시작
    MST = [[0] * N for _ in range(N)]

    while pq:
        row, col = heappop(pq)

        # 이미 방문했으면 continue
        if MST[row][col]:
            continue
        
        MST[row][col] = 1

        for dx, dy in dir:
            nx = row + dx
            ny = col + dy
            # 범위 내이고, 방문하지 않았을 때
            if 0 <= nx < N and 0 <= ny < N and not MST[nx][ny]:
                # 높이 차이가 같으면 +1
                if arr[x][y] == arr[nx][ny]:
                    cnt += 1
                    
                # 다르면 +1에 차이만큼 더 더해줌
                else:
                    cnt += (1 + abs(arr[x][y] - arr[nx][ny]))
                    

                    
      

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()) for _ in range(N))
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우

