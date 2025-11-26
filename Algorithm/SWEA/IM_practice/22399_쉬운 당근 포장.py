T = int(input())

# 대, 중, 소 상자로 구분해 포장해야 한다.
# 같은 크기의 당근은 같은 상자에 들어있어야 한다.
# 비어 있는 상자가 있으면 안 된다.
# 당근의 개수 차이가 최소가 되도록 포장
# 포장 할 수 없는 경우 -1, 포장할 수 있으면 상자에 들어있는 당근의 개수 차이가 최소일 때의 차이값을 출력
for test_case in range(1, T+1):
    N = int(input())  # N개의 당근
    carrots = map(int, input().split())  # 당근 크기들
    carrots.sort() # 크기 순서대로 정렬 => 같은 크기는 붙게 됨!

    diff = 0  # 최소 개수 차이 저장할 변수

    # 최소 1개는 소박스에 들어가야 하므로 i는 1부터 시작함
    # 최소 1개는 대박스에 들어가야 하므로 i는 N-2까지만 가능함
    # i: 소박스와 중박스의 경계 위치
    for i in range(1, N-1):

        if carrots[i-1] == carrots[i]:
            continue

        for j in range(i+1, N):
            if carrots[j-1] == carrots[j]:
                continue

            small_cnt = i
            middle_cnt = j - i
            large_cnt = N - j

            if small_cnt == 0 or middle_cnt == 0 or large_cnt == 0:
                continue

            diff = max(small_cnt, middle_cnt, large_cnt) - min(small_cnt, middle_cnt, large_cnt)

            # 최소 차이값 갱신
            if diff < min_diff:
                min_diff = diff
                possible = True

    # 결과 출력
    if possible:
        print(min_diff)  # 최소 차이 출력
    else:
        print(-1)  # 포장 불가능
