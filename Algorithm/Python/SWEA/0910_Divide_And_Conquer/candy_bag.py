# N종류의 사탕이 있고, 각 종류마다 A1,A2,…,AN개의 사탕이 있다.
# [조건]
# - 가방 안에 정확히 M개의 사탕이 들어 있어야 한다.
# - 모든 가방에 들어 있는 사탕 종류의 구성이 같아야 한다.
# 최대 몇 개의 사탕 가방을 만들 수 있는지 구하는 프로그램 작성

T = int(input())

for test_case in range(1, T+1):
    # N: 사탕 종류의 개수
    # M: 사탕 가방 안에 정확히 M개의 사탕이 들어있어야 함
    N, M = map(int, input().split())
    candy = list(map(int, input().split()))

    # 가방을 몇 개 써야 n개의 똑같은 비율의 사탕 개수가 들어갈 수 있나?

    left = 1
    # 가장 많은 사탕 종류 기준
    # 그 사탕을 가방에 1개씩만 넣으면 이게 최대
    right = max(candy)

    # 이진 탐색
    while left <= right:
        # 가방 개수 = mid
        mid = (left + right) // 2

        # 가방 개수가 mid개라고 할 때
        # 가방 안에 문제의 조건을 맞춰서 사탕 개수를 몇 개 넣을 수 있는가
        cnt = 0
        # i번 사탕
        for i in range(N):
            # i번 사탕을 가방의 개수만큼 나눠야
            # 모든 가방 안에 있는 사탕 비율이 같다
            cnt += candy[i] // mid

        # cnt가 답이 되는지 안되는지 확인
        # 문제에서 원하는 것은 cnt가 정확히 M

        if cnt < M:
            # 세어봤는데 문제에서 원하는 M개보다 작다
            # 사탕 가방의 개수를 줄여야 한다.
            # 계속 왼쪽으로 갔다는 것은 답이 될 가능성이 없다 xxx
            right = mid - 1
        else:
            # 세어봤는데 문제에서 원하는 M개보다 많았다
            # 사탕 가방의 개수를 늘려볼 수 있겠다
            # 최소 답은 right로 확정
            left = mid + 1

    print(f'#{test_case} {right}')