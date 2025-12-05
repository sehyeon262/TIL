# N: 정수 개수, S: 총 합의 정수
N, S = map(int, input().split())
num = list(map(int, input().split()))

# 정답 개수
cnt = 0

# i : 현재 인덱스 (0 ~ N)
# sum_v : 선택한 원소들의 합
# empty : 공집합 확인용! => 크기가 양수인 부분수열이 조건이므로
# - 공집합은 항상 0 => S = 0일 경우 정답에 더해짐  
def dfs(i, sum_v, empty):

    global cnt
    # 모든 인덱스를 다 확인했다면,
    if i == N:
        # 공집합이 아니고(empty = True), 합이 S이면 정답 +1
        if empty and sum_v == S:
            cnt += 1
        # 지금 경로 탐색 종료
        return
    
    # 분기 1) 현재 원소 num[i]를 선택하는 경우
    # 합에 num[i]를 더하고
    # empty를 True로 바꿔서 '하나 이상 선택함'을 표시함
    dfs(i+1, sum_v + num[i], True)

    # 분기 2) 현재 원소 num[i]를 선택하지 않는 경우
    # 합은 그대로 유지하고
    # empty는 이전 값 유지
    dfs(i+1, sum_v, empty)

    # 위 두 호출로, i번째 원소에 대해 "고른다/안 고른다" 두 가지 경우를 모두 탐색함
    # 이 과정을 0 ~ N-1까지 반복하면 가능한 모든 부분집합(2^N개)을 방문하게 됨

# 아직 아무것도 안 골랐으니 False!
dfs(0, 0, False)
print(cnt)
