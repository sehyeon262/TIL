# # 종료 조건: N개의 행을 모두 고려하면 종료
# # 가지의 수: N개의 열
# def recur(row):
#     if row == N:
#         print(*path)
#         return
#     # N개의 열을 보면서
#     for col in range(N):
#         # 사용한 적이 있다면 넘어가기
#         if visited[col]:
#             continue
#
#         # col 선택했다
#         visited[col] = 1
#         path.append(col)
#         recur(row + 1)  # 다음 재귀호출
#         path.pop()  # 되돌아가기 위해
#         visited[col] = 0
#
# N = 4
# answer = 0  # 가능한 정답 수
# path = []   # 임시변수 (경로 출력을 위해)
# visited = [0] * N
# recur(0)

# ------------------------------------------
def check(row, col):
    # 1.같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]:     # 같은 행에 놓은 적이 있다면
            return False

    # 2. 좌상단 대각선에 놓은 적이 있는가? (\) => 시간 오래 걸리는 부분
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # [참고] for 문으로 하고싶다! (고난도)
    # for i, j in zip(range(row - 1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? (/)
    i, j = row - 1, col + 1     # 행은 1개 빠지고, 열은 1개 더해지고
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    return True


# 종료 조건: N개의 행을 모두 고려하면 종료
# 가지의 수: N개의 열
def recur(row):
    global answer
    if row == N:
        answer += 1
        return
    # N개의 열을 보면서
    for col in range(N):
        # 가지치기: 같은 열을 못 고르도록
        # --> 유망하지 않은 케이스를 모두 삭제 (세로, 대각선)
        if check(row, col) is False:    # 행, 열 검사했을 때 False이면 넘어감
            continue

        # col 선택했다
        visited[row][col] = 1
        recur(row + 1)  # 다음 재귀호출
        visited[row][col] = 0


N = 4
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')

N = 20
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')