# 1 ~ 12 가진 부분집합 A
# 집합 A의 부분 집합 중 N개의 원소 가지고,
# 원소의 합이 K인 부분집합 개수 출력
# 해당하는 부분집합 없는 경우 0 출력!

def powerset(i, n, sum_v):
    # i: A에서 현재 보고 있는 인덱스
    # n: 지금까지 고른 원소 개수
    # sum_v: 지금까지 고른 원소의 합
    global cnt

    # 가지치기
    if sum_v > K:   # 이미 합이 K를 넘었으면 종료!
        return
    if n + (12 - i) < N:    # 남은 걸 다 골라도 N개를 못 채우면 종료!
        return

    # 숫자 12개를 다 보았으면 종료
    if i == 12:
        if n == N and sum_v == K:
            cnt += 1
        return

    # 정확히 N개를 골랐을 때 합이 K면 카운트 (선택사항임)
    if n == N:
        if sum_v == K:
            cnt += 1
        return

    # 재귀 호출
    powerset(i + 1, n + 1, sum_v + A[i])    # 원소 선택한 경우
    powerset(i + 1, n, sum_v)           # 원소 선택하지 않은 경우

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N: 부분집합 개수, K: 원소의 합
    cnt = 0
    A = list(range(1, 13))
    powerset(0, 0, 0)
    print(f'#{test_case} {cnt}')
