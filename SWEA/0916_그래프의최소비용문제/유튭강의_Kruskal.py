import sys
sys.stdin = open("MST_input.txt", "r")

def find_set(x):
    if x == parents[x]:
        return x
    # 기본 코드
    # return find_set(parents[x])

    # 경로 압축
    # find_set(parents[x])    # 대표자가 return
    parents[x] = find_set(parents[x])
    return parents[x]

#  유니온 파인드 필요 3가지
# - 집합생성
# - 대표자 찾기
# - 병합
def union(x, y):
    # 대표 데리고와
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:    # 사이클 발생
        return

    # 일정한 규칙으로 병합 (더 작은 수로)
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))  # 간선들의 정보를 저장

# 가중치(weight) 기준으로 오름차순
edges.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택하자
# - 와중에 사이클이 발생하면 고르지 말자!
# - 언제까지?
#   => MST가 완성될 때까지
#     = V-1 개를 선택할 때까지
cnt = 0     # 현재까지 선택한 간선의 수
result = 0  # 가중치의 합

parents = [i for i in range(V)]     # make_set


# 간선들을 하나씩 꺼냄
for u, v, w in edges:
    # 사이클이 아니라면
    # - 연결(같은 집합으로 만든다) => 그래프를 생성하겠다는 건 아님!!!
    # - cnt += 1
    # - cnt가 V - 1이라면 종료
    if find_set(u) != find_set(v):  # u, v 사이클이 아니라면:
        print(u, v, w)
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break
print(f'최소 비용 = {result}')
