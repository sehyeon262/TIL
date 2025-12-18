# i : 행 번호, j : 열 번호
def solve(i, j, sum_v):
    global min_sum
    # 현재 칸 더함
    sum_v += arr[i][j]
    # 가지치기
    if sum_v >= min_sum:
        return

    # 도착했다면 갱신!
    if (i, j) == (N-1, N-1):
        min_sum = sum_v
        return

    # 재귀 (다음 단계)
    # 오른쪽
    if j + 1 < N:
        solve(i, j + 1, sum_v)
    # 아래
    if i + 1 < N:
        solve(i + 1, j, sum_v)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')

    # 재귀 호출
    solve(0, 0, 0)
    print(f'#{test_case} {min_sum}')