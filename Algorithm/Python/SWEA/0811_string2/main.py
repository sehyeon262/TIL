T = 10  # 테스트케이스 개수

# 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제
# 가장 긴 회문의 길이 출력

for test_case in range(1, T+1):
    arr = [list(input()) for _ in range(100)]
    max_v = 0  # 가장 긴 회문의 길이

    # 행 탐색
    for i in range(100):
        for start in range(100):
            for end in range(start, 100):
                row = arr[i][start:end+1]
                if row == row[::-1]:
                    if max_v < len(row):
                        max_v = len(row)

    # 열 검색
    for i in range(100):
        for start in range(100):
            for end in range(start, 100):
                col = [arr[x][i] for x in range(start, end+1)]
                if col == col[::-1]:
                    if max_v < len(col):
                        max_v = len(col)

    print(f'{test_case} {max_v}')