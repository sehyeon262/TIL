arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def recur(cnt):
    # 종료 조건 (3명을 모두 고려)
    if cnt == 3:
        print(*path)
        return


    # 재귀호출 파트
    # - 부분집합에 포함되는 경우 (O를 추가)
    path.append(arr[0])
    recur(cnt + 1)
    path.pop()  # 돌아갈때 마지막에 추가한 'O'를 빼주자

    # - 포함되지 않는 경우 (X를 추가)
    path.append(arr[1])
    recur(cnt+1)
    path.pop()

recur(0)    # 0명을 고려한 상태로 시작

# --------- 실제 많이 보게 될 코드 ---------
# name = ['MIN', 'CO', 'TIM']
#
# # 두 번째 선택에서는
# # 'MIN'이라는 친구가 포함된 상태를 저장하면서 진행 할 수 없을까?
# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return
#
#     # 부분집합에 포함 시키는 경우
#     recur(cnt + 1, subset + [name[cnt]])
#     # 포함 시키지 않은 경우
#     recur(cnt + 1, subset)
#
#
# # 시작은 아무도 포함되지 않았으니깐 빈 리스트
# recur(0, [])