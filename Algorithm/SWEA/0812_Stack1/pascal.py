T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(N):
        # i번째 줄에는 i + 1개의 원소가 있음
        # 처음과 끝은 1로 채움
        arr.append([1] * (i + 1))

        # 첫 번째 원소와 마지막 원소를 제외한 원소들 계산
        for j in range(1, i):
            # 바로 윗줄(i-1)의 j-1번째 원소 + j번째 원소 합
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]


    print(f'#{test_case}')
    for i in range(N):
        # join은 문자열을 하나씩 붙여주는 것이므로 바꿔줘야함
        print(' '.join(map(str, arr[i])))



