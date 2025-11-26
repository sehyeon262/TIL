N = 10

p = [0] * (N + 1)

# 초기화 연산
# x 자기 자신이 대표인 집합을 만든다.
def make_set(x):
    p[x] = x

# x가 속한 집합의 대표가 누구냐?
def find_set(x):
    if p[x] == x:
        return x
    return find_set(p[x])


# 경로 압축 버전
# 모든 x에 대해서 find_set