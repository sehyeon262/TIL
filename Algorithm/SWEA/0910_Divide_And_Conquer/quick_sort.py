def quick_sort(left, right):
    if left < right:    # 양쪽에서 오다가 교차하면 종료하므로
        pivot = hoare(left, right)
        '''
        hoare를 돌고 나면 pivot이 인덱스 p에 "최종 차리"로 고정되니깐,
        pivot은 더이상 건드릴 필요 없어서 p를 빼고 왼쪽(left..p-1), 오른쪽만 다시 정렬(p+1..right)
        [left .. p-1]   [ p ]   [p+1 .. right]
            ≤ pivot     pivot       ≥ pivot

        '''
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


def hoare(left, right):
    mid = (left + right) // 2
    pivot = A[mid]  # 피벗을 중간 요소로 설정
    A[left], A[mid] = A[mid], A[left]
    # 포인터 설정
    i = left + 1
    j = right

    while i <= j:
        while i <= j and A[i] <= pivot:     # 왼쪽에서 출발
            i += 1                          # pivot 이하(제자리)는 패스하고,
                                            # 처음으로 'pivot보다 큰 값'에서 멈춤
        while i <= j and A[j] >= pivot:     # 오른쪽에서 출발
            j -= 1                          # pivot 이상(제자리)은 패스하고,
                                            # 처음으로 'pivot보다 작은 값'에서 멈춤
        if i < j:
            A[i], A[j] = A[j], A[i]
        '''
        두 스캔이 끝난 순간(그리고 i<j라면) 항상
        * A[i] > pivot → 왼쪽에 있으면 안 되는 큰 값,
        * A[j] < pivot → 오른쪽에 있으면 안 되는 작은 값
        이렇게 “서로 뒤바뀐 한 쌍”이 잡혀있음
    
        그래서 i < j면 그 둘을 스왑해서
        * 큰 값은 오른쪽으로,
        * 작은 값은 왼쪽으로 보냄.
        한 번의 스왑으로 두 문제를 동시에 해결!
        '''

    # 교차하면 j랑 pivot이랑 바꿔줌
    A[left], A[j] = A[j], A[left]
    return j

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, len(A) - 1)
    print(f'#{test_case} {A[N//2]}')