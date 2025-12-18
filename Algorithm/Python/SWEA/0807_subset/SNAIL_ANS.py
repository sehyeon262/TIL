def slug(N):
    # 숫자를 넣을 배열 생성
    matrix = [[0] * N for _ in range(N)]


# dleta
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 행렬에 넣을 숫자
cnt = 0
# 행
i = 0
# 열
j = 0
# delta 이동 방향
direction = 0

# cnt가 N의 제곱이 될때 까지 반복
while True:
    cnt += 1
    matrix[i][j] = cnt

    ni = i + di[direction]
    nj = j + dj[direction]

    if not (0 <= ni <= N - 1) or not (0 <= nj <= N - 1) or (matrix[ni][nj] != 0):
        direction += 1
        if direction == 4:
            direction = 0
        ni = i + di[direction]
        nj = j + dj[direction]

    i = ni
    j = nj

    if cnt == N ** 2:
        break
return matrix
