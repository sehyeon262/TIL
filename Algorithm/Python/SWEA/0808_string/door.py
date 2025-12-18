T = int(input())

def find_string(arr, N, M):
    # 가로 방향 탐색
    for i in range(N):  # 각 행 하나씩 선택함
        # 시작 인덱스 고정 => i번째 행에서 j번째 열부터 M개의 문자 자름
        for j in range(N - M + 1):
            # M길이 슬라이스
            row = arr[i][j:j+M]
            # 회문 판별(뒤집은 문자와 같은면 회문)
            if row == row[::-1]:
                # 회문이면 반환
                return row

    # 세로 방향 탐색
    for i in range(N):  # 각 열을 하나씩 선택함
        for j in range(N - M + 1):
            # j번째 행부터 M개의 문자 세로 방향으로 뽑아서 리스트 만듦
            col = [arr[j+k][i] for k in range(M)]
            # 회문 판별(뒤집은 문자와 같은면 회문)
            if col == col[::-1]:
                # 리스트를 문자열로 합쳐서 반환
                return ''.join(col)


for test_case in range(1, T+1):
    # N x N 배열 , M: 찾을 회문 길이
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = find_string(arr, N, M)
    print(f'{test_case} {result}')
