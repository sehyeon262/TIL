T= int(input())

for test_case in range(1, T+1):
    N = int(input())  # 칠 할 영역의 개수
    board = [[0] * 10 for _ in range(10)]  # 10 x 10 2차원 배열 준비
    purple_count = 0  # 3이 되면 보라색으로 판단하는 변수 설정

    for _ in range(N):
        r1, c1, r2, c2, c = list(map(int, input().split()))
        for i in range(r1, r2+1):  # 행 순환
            for j in range(c1, c2+1):  # 열 순환

                if board[i][j] == 1 and c == 2:
                    board[i][j] = 3  # 보라색
                    purple_count += 1
                elif board[i][j] == 2 and c == 1:
                    board[i][j] = 3  # 보라색
                    purple_count += 1
                elif board[i][j] == 0:
                    board[i][j] = c  # 그냥 색칠

    print(f'#{test_case} {purple_count}')

