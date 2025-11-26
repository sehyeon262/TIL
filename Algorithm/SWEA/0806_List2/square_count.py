T = int(input())

# 가로 길이가 N인 정사각형 안에 크기가 M인 정사각형이 몇 개 들어 있나?
# 크기가 M인 정사각형 하나 만들때마다 숫자를 격자판에 기록
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    square_count = 1  # 가로 크기가 N인 정사각형 안의 M x M 정사각형 개수
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for x in range(M):
                for y in range(M):
                    board[i + x][j + y] = square_count
            # M x M 정사각형 다 찾고 난 후 개수에 +1씩 해줌
            square_count += 1

    result = ''
    # 이중 반복문을 통해 2차원 리스트 board의 모든 요소를 순회
    print(f'#{test_case}')
    for row in board:
        # 1차원씩 꺼내서 원소 하나하나를 str로 만들어서 공백으로 이어 붙임
        print(' '.join(map(str, row)))  # 한 줄씩 공백 구분해서 출력

