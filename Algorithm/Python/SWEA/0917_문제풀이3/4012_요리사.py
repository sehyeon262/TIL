# 재귀호출 필수 => 종료조건, 가지치기

def get_synergy():
    pass



# 종료 조건: 재료의 반을 선택 --> 시너지 계산
# 가지의 수: 모든 재료(N)
def recur(cnt, prev):
    if cnt == N // 2:
        a_total, b_total = get_synergy()
        min_v
        return
    
    for food_num in range(prev + 1, N):     # 바나나를 골랐으면 바나나 다음 걸 고름
        if visited[food_num]:   # 이미 선택했으면 continue
            continue

        visited[food_num] = 1
        recur(cnt + 1, food_num)
        visited[food_num] = 0




T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_v = 0
    recur()
    print(f'#{test_case} {min_v}')