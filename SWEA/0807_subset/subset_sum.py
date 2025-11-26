T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# A의 부분집합 중 N개의 원소를 갖고
# 원소의 합이 K인 부분집합의 개수 출력
# 해당하는 부분집합 없는 경우 0 출력
# EX) N=3, K=6 => 부분집합 {1,2,3} 1가지 존재

for test_case in range(1, T+1):
    N, K = map(int, input().split())  # N: 부분집합 원소의 수, K: 부분집합의 합
    arr = []
    subset_count = 0  # 해당하는 부분집합 개수

    for i in range(1 << len(A)):  # 부분 집합의 개수
        count = 0  # 부분집합 원소 개수
        sum_subset = 0  # 부분집합 원소 합

        for j in range(len(A)):  # 원소의 수만큼 비트 비교
            if i & (1 << j):  # i의 j번째 비트가 1인 경우
                arr.append(A[j])
                count += 1
                sum_subset += A[j]

        # 정답 조건
        if count == N and sum_subset == K:
            subset_count += 1

    if subset_count > 0:
        print(f'#{test_case} {subset_count}')
    else:
        print(f'#{test_case} 0')


