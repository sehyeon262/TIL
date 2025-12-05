# 정수 0 ~ 9
# 연산자: (+, - , *) => 우선순위 모두 동일하므로 왼쪽에서부터 순서대로 계산함
# 괄호 안에는 연산자가 하나만 들어있어야 함
# 중첩 괄호 사용 ㄴㄴ

N = int(input())    # 정수와 연산자 개수
arr = list(input())

num_lst = []    # 숫자 리스트
oper_lst = []   # 연산자 리스트

# 숫자와 연산자를 나눠줌
for x in arr:
    if x.isdigit(): 
        num_lst.append(arr[i])
    else:
        oper_lst.append(arr[i])

max_v = -float('inf')

# n_idx: 다음에 사용할 연산자 인덱스
# cur_val: (n_idx - 1)번째까지 계산된 결과 값
def dfs(n_idx, cur_val):


