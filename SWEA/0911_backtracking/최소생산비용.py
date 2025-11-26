#  N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램
def min_cost(row, sum_v):
    global min_v

    # 기저 조건
    if row == N:
        min_v = min(min_v, sum_v)
        return

    # 이미 최소값을 넘었으면 종료
    if min_v <= sum_v:
        return
    # 현재 행에 배정할 열을 하나 고름
    # 한 열을 한 번만 사용할 수 있으므로 visited로 중복 방지
    for col in range(N):
        # 이미 다른 행이 이 열을 썼다면 skip
        if visited[col]:
            continue
        visited[col] = 1    # 열 사용했다고 표시하고
        min_cost(row + 1, sum_v + arr[row][col])    # 다음 행(row+1)으로 내려가며, 비용 누적함
        visited[col] = 0    # 원상복구!


T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')    # 최솟값을 무한대로 설정
    sum_v = 0   # 합
    visited = [0] * N   # 열(col)을 사용 했는지 여부
    min_cost(0, 0)
    print(f'#{test_case} {min_v}')
