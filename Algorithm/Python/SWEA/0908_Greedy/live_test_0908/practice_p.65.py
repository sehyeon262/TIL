N = 10

numbers = [-1,3,-9,6,7,-6,1,5,4,-2]
cnt = 0

# 부분집합을 구하는 재귀함수
# id번 인덱스에 있는 원소를 부분집합에 포함o or 포함 x
# selected : 우리가 지금까지 포함한 원소들
def subset(idx, selected):
    global cnt
    # 종료
    # 10번 선택을 모두 완료 => 종료
    if idx == N:
        # 그 중에 합이 0인 부분 집합만 골라서 출력
        if sum(selected) == 0:
            cnt += 1
            print(selected)
        return

    

    # 재귀호출
    # 2가지로 나뉨
    # idx번 원소를 부분집합에 포함하고 idx+1 단계로 이동
    # idx 원소를 부분집합에 포함하지 않고 idx+1 단계로 이동
    subset(idx + 1, selected + [numbers[idx]])  # 원소가 하나인 리스트 이어붙임
    subset(idx + 1, selected)

    # selected.pop()이랑 append 할 필요 없는 이유?

subset(0, [])
print(cnt)