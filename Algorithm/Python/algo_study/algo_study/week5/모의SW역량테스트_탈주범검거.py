from collections import deque

# 파이프 터널 타입대로 이동 가능한 방향 저장함
tunnel = {
    1: [[-1, 0], [1, 0], [0, -1], [0, 1]],    # 상하좌우
    2: [[-1, 0], [1, 0]],                     # 상하
    3: [[0, -1], [0, 1]],                     # 좌우
    4: [[-1, 0], [0, 1]],                     # 상우
    5: [[1, 0], [0, 1]],                      # 하우
    6: [[1, 0], [0, -1]],                     # 하좌
    7: [[-1, 0], [0, -1]],                    # 상좌
}
    

T = int(input())
for test_case in range(1, T+1):
    # N x M배열, R: 뚜껑 세로 위치(행), C: 뚜껑 가로 위치(열), L: 탈출 후 소요시간
    N, M, R, C, L = map(int, input().split())
    hole = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    
    q = deque([(R, C, 1)])    # 시작 시간은 1임 => 한 시간 뒤에 뚜껑에 도착했으므로!
    visited[R][C] = 1   # 뚜껑 자리 방문
    cnt = 1     # 시작 칸 카운트 포함

    while q:
        r, c, t = q.popleft()
        
        # 파이프가 없으면 건너뛰고
        if hole[r][c] == 0:
            continue

        # 파이프 모양에 따른 이동방향
        for dr, dc in tunnel[hole[r][c]]:
            nr = r + dr
            nc = c + dc

            # 인덱스 범위 안이고, 파이프가 존재하고, 시간 안이고, 방문한 적 없으면,
            if 0 <= nr < N and 0<= nc < M and hole[nr][nc] and t < L and not visited[nr][nc]:
                # 다음 이동 위치 파이프 확인
                for ndr, ndc in tunnel[hole[nr][nc]]:
                    # 현재 칸에서 나가는 방향이 다음 칸에서 들어가는 방향과 부호가 반대여야함! (=맞물린거임)
                    if (dr + ndr == 0) and (dc + ndc == 0):
                        visited[nr][nc] = 1
                        cnt += 1
                        q.append((nr, nc, t+1))
                        break
    
    print(f'{test_case} {cnt}')
