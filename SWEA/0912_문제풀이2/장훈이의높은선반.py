# 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 
# 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
# 탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 
# 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 "높이가 가장 낮은 탑"을 알아내려고 한다.
# 만들 수 있는 높이가 B 이상인 탑 중에서 "탑의 높이와 B의 차이가 가장 작은 것"을 출력한다

def recur(cnt, sum_v):
    global min_v
    
    # 목표 도달
    if sum_v >= B:
        diff = sum_v - B
        if diff < min_v:
            min_v = diff
        return
    
    # 종료 조건
    if cnt == N:
        return

    recur(cnt + 1, sum_v + height[cnt]) # 포함
    recur(cnt + 1, sum_v)               # 미포함
    

T = int(input())
for test_case in range(1, T+1):
    # N: 점원 수, B: 선반 높이
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort(reverse = True)   # 가지치기 효율위해 큰 키부터 시도함(내림차순)
    min_v = float('inf')
    recur(0, 0)
    print(f'#{test_case} {min_v}')
    

# ---------------------------------------

def solve_one(N, B, H):
    # 가지치기 효율을 위해 큰 키부터 시도(빨리 B를 넘겨서 min_v를 줄여놓기)
    H.sort(reverse=True)

    # suffix[i] = i번째 이후(포함) 키 합
    suffix = [0]*(N+1)
    for i in range(N-1, -1, -1):
        suffix[i] = suffix[i+1] + H[i]

    min_v = float('inf')  # (탑 높이 - B)의 최소값

    def dfs(i, sum_v):
        nonlocal min_v

        # 1) 목표 도달: 합이 B 이상이면 차이를 갱신하고 더 내려갈 필요 없음
        if sum_v >= B:
            diff = sum_v - B
            if diff < min_v:
                min_v = diff
            return

        # 2) 끝까지 봤으면 종료
        if i == N:
            return

        # 3) 이미 현재 합 기준 차이가 최적보다 나쁘면 가지치기
        # (sum_v < B라서 sum_v - B는 음수지만, 이후에 H[i]를 더해도
        #  어차피 최소 차이 min_v보다 작게 만들 가능성이 없을 때 컷)
        if (B - sum_v) <= 0 and (sum_v - B) >= min_v:
            return

        # 4) 남은 키 전부 더해도 B를 못 넘으면 더 볼 가치 없음 (상한 가지치기)
        if sum_v + suffix[i] < B:
            return

        # 포함/미포함 분기
        dfs(i + 1, sum_v + H[i])  # i번째 점원 포함
        dfs(i + 1, sum_v)         # i번째 점원 미포함

    dfs(0, 0)
    return min_v

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = solve_one(N, B, H)
    print(f'#{tc} {ans}')


# ---------------------------------------
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     H = list(map(int, input().split()))

#     # dp의 k번째 비트가 1이면 "합 k를 만들 수 있다"는 뜻
#     dp = 1  # 합 0 가능
#     for h in H:
#         dp |= (dp << h)  # h를 더해 만들 수 있는 합들을 켠다

#     # B 이상 중에서 가장 작은 합 찾기
#     # y = dp를 B만큼 오른쪽으로 민 값 → y의 0번째 비트가 "합 B 가능" 의미
#     y = dp >> B

#     if y == 0:  # (안전장치) 어떤 부분집합도 B 이상을 못 만들 때
#         diff = B - sum(H)
#     else:
#         # y의 최하위 1비트 위치 = (최소 초과분)
#         diff = (y & -y).bit_length() - 1

#     print(f'#{tc} {diff}')


