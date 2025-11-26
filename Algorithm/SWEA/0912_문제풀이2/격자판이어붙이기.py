# ---------- 라이브 코드 -------------

# 격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램

# <문제에서 알 수 있는 것>
# 1. 델타 배열
# 2. visited 안 쓴다
# 3. 서로 다른 수 => set() 사용
# 4. 6번 이동

# 1. 종료: 6번
# 2. 가지의 수: 4개 (상하좌우)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 1. 종료조건: 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):    # 7자리면 종료
    if len(number) == 7:    # set에 추가
        result.add(number)
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 범위 밖이면 continue
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        # 다음 위치로 이동
        # 다음으로 넘어갈 때 숫자 누적해줌1
        recur(ny, nx, number + matrix[ny][nx])        


T = int(input())
for test_case in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()  # lsit, set 등 값을 추가하는 구조 아님객체 형태

    # 7자리 만드는 코드
    # -4 x 4가 모두 출발점이 될 수 있다
    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, matrix[sy][sx])   # 좌표랑 숫자 같이 줌


    print(f'#{test_case} {len(result)}')

# ---------------- 내가 연습한 코드-------------------

# 격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 
# 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다
# 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, => visited 필요 없음!
# 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
# 격자판을 벗어나는 이동은 가능하지 않다고 가정한다. => 범위 구현!
# 만들 수 있는 "서로 다른 일곱 자리 수"들의 개수를 구하는 프로그램을 작성 => set 사용!

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우

def move(sx, sy, number):
    # 종료 조건
    # 7자리 완성했으면 set에 넣어주고 종료함!
    if len(number) == 7:
        result.add(number)
        return
    
    for i, j in dir:
        nx = sx + i
        ny = sy + j
        # 범위 밖이면
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue
        # 범위 안이면 다음 위치로 이동
        # 숫자 누적해서 이동
        move(nx, ny, number + grid[nx][ny])
    

T = int(input())
for test_case in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()

    for sx in range(4):
        for sy in range(4):
            move(sx, sy, grid[sx][sy])  # 좌표랑 숫자 같이 줌
    
    print(f'#{test_case} {len(result)}')
    

