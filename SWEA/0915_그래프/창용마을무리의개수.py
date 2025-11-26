# 대표자 찾는 함수
def find_set(x):
    if x == par[x]: # 자기자신이 대표자면
        return x
    
    par[x] = find_set(par[x])
    return find_set(par[x])

# 합집합
def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 경로 압축!!
    if rep_x != rep_y:
        par[rep_y] = rep_x


T = int(input())
for test_case in range(1, T+1):
    # N: 창용마을 사람 수, M: 서로를 알고 있는 사람의 관계 수
    N, M = map(int, input().split())
    graph = [0] * (N + 1)

    # 자기 자신이 대표자라 설정하고 집합 만듦
    par = [i for i in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    cnt = set()
    for i in range(1, N+1):
        a = find_set(i)
        cnt.add(a)
    
    print(f'#{test_case} {len(cnt)}')
