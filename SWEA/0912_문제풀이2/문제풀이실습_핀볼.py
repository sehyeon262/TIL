import sys
sys.stdin = open("sample_input.txt")

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dir_dict = {
    (-1, 0): 0, # 상
    (0, 1): 1,  # 우
    (1, 0): 2,  # 하
    (0, -1): 3  # 좌
}


def dir_search(nx, ny, d):
    if arr[nx][ny] == 1:
        if d == 0:      # 상
            d = 2
        elif d == 1:    # 우
            d = 3
        elif d == 2:    # 하
            d = 1
        else:           # 좌
            d = 0
        return d
    
    if arr[nx][ny] == 2:
        if d == 0:      # 상
            d = 1
        elif d == 1:    # 우
            d = 3
        elif d == 2:    # 하
            d = 0
        else:           # 좌
            d = 2
        return d

    if arr[nx][ny] == 3:
        if d == 0:      # 상
            d = 3
        elif d == 1:    # 우
            d = 2
        elif d == 2:    # 하
            d = 0
        else:           # 좌
            d = 1
        return d
    
    if arr[nx][ny] == 4:
        if d == 0:      # 상
            d = 2
        elif d == 1:    # 우
            d = 0
        elif d == 2:    # 하
            d = 3
        else:           # 좌
            d = 1
        return d

    if arr[nx][ny] == 5:
        if d == 0:      # 상
            d = 2
        elif d == 1:    # 우
            d = 3
        elif d == 2:    # 하
            d = 0
        else:           # 좌
            d = 1
        return d

def hole(nx, ny):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == arr[nx][ny]:
                if (i, j) != (nx, ny):
                    return i, j
            


def game(si, sj, d):    # 출발 좌표: si, sj
    global score

    while True:
        
        for dx, dy in dir:
            nx = si + dx
            ny = sj + dy
            d = dir_dict[(nx, ny)]

            # 벽에 부딫히면 방향을 바꾸고, 점수 +1
            if not(0 <= nx < N and 0 <= ny < N):
                d = (d + 2) % 4
                score += 1
                game(nx, ny, )
            else:   # 범위 안 이면
                if arr[nx][ny] == 0:    # 0이면
                    continue
                elif 1 <= arr[nx][ny] <= 5: # 블록이면
                    score += 1
                    d = dir_search(nx, ny, d)
                    game(nx, ny, d)
                else:   # 웜홀이면
                    a, b = hole(nx, ny)
                    game(a, b, d)
            if arr[nx][ny] != arr[si][sj] or arr[nx][ny] != -1:
                break 
    return


# -------- 메인 -----------
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = 0   # 점수
    max_v = 0

    # 출발 좌표를 찾자!
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:  # 출발좌표부터 시작!
                for d in range(4):
                    game(i, j, d)
                    if max_v < score:
                        max_v = score
                        
    
    print(f'#{test_case} {score}')

# ------------------------------------------------------------------------

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    worm_hole = {}

    # 웜홀 쌍 찾기
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                hol_num = arr[i][j]
