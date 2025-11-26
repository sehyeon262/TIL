# 1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때
# 전체 몇 개의 조가 만들어지는지 출력하는 프로그램


'''
서로소 집합은 연결 정보들을 합치고,
최종적으로 '그룹의 개수'를 세는 프로그램임

- make_set :  각 원소를 자기 자신이 대표(부모)인 집합으로 초기화
- find_set : 원소가 속한 집합의 "대표(루트)"를 찾음
- union : 두 원소가 속한 집합을 합침 
'''

def make_set(n):
    # 1 ~ n까지의 원소가 "각자 자기 자신이 대표자라고 설정" = 집합을 만듦
    # n + 1인 이유 => 문제에서 정점 번호가 1 ~ n을 쓰는 경우가 많기 때문
    return [i for i in range(n + 1)]


# 집합의 대표자를 찾는 함수
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == par[x]:
        return x
    
    # 경로 압축 !!!!!!!!!!!!
    # - 내 부모를 대표자로 바로 가리키도록
    par[x] = find_set(par[x])
    return find_set(par[x])


def union(x, y):
    # x, y의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 다른 집합이면 합치기
    if rep_x != rep_y:
        par[rep_y] = rep_x  
    
    

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    par = make_set(N)

    # M개의 (u, v) 쌍에 대해 집합을 합침
    for i in range(M):
        u = arr[2 * i]
        v = arr[2 * i + 1]
        union(u,v)

    # 최종적으로 서로 다른 대표(루트)의 개수가 곧 그룹의 개수
    cnt = set()
    for j in range(1, N+1):
        a = find_set(j)     # j가 속한 집합의 대표
        cnt.add(a)          # 대표들을 집합에 모아 중복 제거
    
    print(f'#{test_case} {len(cnt)}')

