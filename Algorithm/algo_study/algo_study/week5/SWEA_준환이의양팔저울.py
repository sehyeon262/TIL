# 모든 무게 추를 양팔저울 위에 올리는 순서는 총 N!가지
# 여기에 더해서 각 추를 양팔저울의 왼쪽에 올릴 것인지 오른쪽에 올릴 것인지를 정해야 해서 총 2N * N!가지
# 오른쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 더 커져서는 안 된다.
# 양팔 저울에 모든 무게추를 올리는 방법은 총 몇 가지가 있을까?


def factorial(k):
    result = 1
    while k > 1:
        result *= k
        k -= 1
    return result

def dfs(depth, left, right, remain):
    global cnt
    
    # 종료 조건 => 모든 추를 올렸으므로 1가지 완성됨 
    if depth == N:
        cnt += 1
        return 
    
    # 확정 승리 가지치기
    rest = N - depth    # 남은 추의 개수
    # 남은 추를 다 올려도 왼쪽이 크면 순서가 바껴도 항상 성립이므로 경우의 수는 rest!임
    if left >= right + remain:  
        cnt += 2 ** rest * factorial(rest)  
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(depth + 1, left + weight[i], right, remain - weight[i])   # 왼쪽에 올리기
        if right + weight[i] <= left:
            dfs(depth + 1, left, right + weight[i], remain - weight[i])   # 오른쪽에 올리기
        visited[i] = 0   # 원상복구!!!!!

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 무게추 개수
    weight = list(map(int, input().split()))
    weight.sort(reverse=True)   # 무거운 것부터 해서 가지치기 빠르게 하기 위해
    cnt = 0     # 방법 개수
    visited = [0] * N
    remain = sum(weight)
    dfs(0, 0, 0, remain)
    print(f'#{test_case} {cnt}')