# 개구리가 점프할 수 있는 거리는 최대 K
# 물웅덩이의 가장 왼쪽에는 항상 나뭇잎이 떠있다.
# 나뭇잎이 없더라도, 개구리는 무조건 K만큼 점프를 하고 물에 빠지게 된다.
# 개구리는 물웅덩이의 가장 왼쪽에서 점프를 시작
# 개구리가 최대로 이동한 거리가 얼마인지 알아내는 프로그램을 작성하시오.
# 나뭇잎이 있는 곳은 1, 없는 곳은 0

def jump(leaf, i):  # i: 현재 개구리 위치
    # 종료 조건
    if i >= N:
        return N

    # 이번 점프로 도달 가능한 최대 좌표 넘지 않게 해야 함!
    limit = min(i + K, N)

    # i+1 ~ limit 사이에서 '가장 먼 1'을 찾기 위해 뒤에서 부터 탐색
    for j in range(limit, i, -1):
        if leaf[j] == 1:
            return jump(leaf, j)
    # 이 구간에 1이 없다면 물이지만, 이동거리 인정함. (limit까지)
    return jump(leaf, limit)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    leaf = [0] + list(map(int, input().split()))

    cnt = jump(leaf, 1)
    print(f'#{test_case} {cnt}')




