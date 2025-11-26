T = 10

for test_case in range(1, T+1):
    # 찾아야 하는 회문의 길이
    N = int(input())
    # 8 x 8 배열임
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    # 가로 방향 탐색
    for i in range(8):
        # 시작 인덱스 고정 => i번째 행에서 j번째 열부터 N개의 문자 자름
        for j in range(8 - N + 1):
            # N길이 슬라이스
            row = arr[i][j:j+N]
            # 회문 판별(뒤집은 문자와 같으면 회문임)
            if row == row[::-1]:
                cnt += 1

    # 세로 방향 탐색
    for i in range(8):
        for j in range(8 - N + 1):
            # j번째 행부터 N개의 문자를 세로 방향으로 뽑아서 리스트 만듦
            col = [arr[j+k][i] for k in range(N)]
            # 회문 판별(뒤집은 문자와 같으면 회문임)
            if col == col[::-1]:
                cnt += 1

    print(f'#{test_case} {cnt}')

