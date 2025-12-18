# N // 2 번째 원소,
# 오른쪽 원소가 먼저 복사되는 경우(왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우) 출력

# def divide(lst):
#     # 1. 분할
#     if len(lst) == 1:
#         return lst
#
#     mid = len(lst) // 2
#     left = lst[:mid]
#     right = lst[mid:]
#
#     left_lst = divide(left)
#     right_lst = divide(right)
#
#     # 2. 병합
#     merge_lst = merge(left_lst, right_lst)
#     return merge_lst
#
# def merge(left_l, right_l):
#     global cnt
#     result = [0] * (len(left_l) + len(right_l))
#     l = r = 0
#
#     if left_l[-1] > right_l[-1]:    # 오른쪽 원소가 먼저 복사되면 +1
#         cnt += 1
#
#     while l < len(left_l) and r < len(right_l):
#         if left_l[l] < right_l[r]:
#             result[l + r] = left_l[l]
#             l += 1
#         else:   # 오른쪽 원소가 먼저 복사되는 경우
#             result[l + r] = right_l[r]
#             r += 1
#
#     while l < len(left_l):
#         result[l + r] = left_l[l]
#         l += 1
#
#     while r < len(right_l):
#         result[l + r] = right_l[r]
#         r += 1
#
#     return result
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     cnt = 0     # 오른쪽 원소가 먼저 복사되는 경우의 수
#     result_lst = divide(arr)
#     print(f'#{test_case} {result_lst[N//2]} {cnt}')



# ---------- 방법 2 -----------

# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst, 0
#
#     mid = len(lst) // 2
#     left, c1 = merge_sort(lst[:mid])    # 왼쪽 부분 결과, 그 과정의 카운트
#     right, c2 = merge_sort(lst[mid:])   # 오른쪽 부분 결과, 그 과정의 카운트
#     merged, c = merge(left, right)      # 두 정렬된 리스트를 합치면서 추가 카운트 받고
#     return merged, (c1 + c2 + c)        # 전체 카운트를 계산해줌
#
# def merge(L, R):
#     # 이 merge에서 한 번만 세어야 함
#     cnt = 1 if L and R and L[-1] > R[-1] else 0
#
#     i = j = 0
#     res = []
#     while i < len(L) and j < len(R):
#         if L[i] <= R[j]:
#             res.append(L[i])
#             i += 1
#         else:
#             res.append(R[j])
#             j += 1
#     # 남은 리스트 한 번에 복사
#     res.extend(L[i:])
#     res.extend(R[j:])
#     return res, cnt
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     sorted_arr, cnt = merge_sort(arr)
#     print(f'#{tc} {sorted_arr[N // 2]} {cnt}')


# ----- 방법 3 -----
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])    # 왼쪽 부분 결과, 그 과정의 카운트
    right = merge_sort(lst[mid:])   # 오른쪽 부분 결과, 그 과정의 카운트
    merged = merge(left, right)      # 두 정렬된 리스트를 합치면서 추가 카운트 받고
    return merged        # 전체 카운트를 계산해줌

def merge(L, R):
    global cnt
    # 이 merge에서 한 번만 세어야 함
    if L and R and L[-1] > R[-1]:
        cnt += 1

    i = j = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    # 남은 리스트 한 번에 복사
    res.extend(L[i:])
    res.extend(R[j:])
    return res

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N // 2]} {cnt}')