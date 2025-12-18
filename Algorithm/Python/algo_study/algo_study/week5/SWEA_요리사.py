# N // 2 개를 A에 넣고, 나머지는 B라고 가정
# -> 모든 재료를 골라보면서, A에 넣자
# -> visited 로 구현 (1이라면 A에 들어감, 0이라면 B에 들어감)

def cal_syerny(li):
    total = 0

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            total += arr[li[i]][li[j]] + arr[li[j]][li[i]]

    return total


def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

    return cal_syerny(A_list), cal_syerny(B_list)

# 종료조건: 재료의 반을 선택 => 시너지 계산
# 가지의수: 모든 재료(N)
def recur(cnt, prev):
    """
    cnt : 지금까지 A그룹에 넣은 재료 개수
    prev: 바로 직전에 A그룹에 넣은 '재료 번호'
          → 다음 선택은 range(prev+1, N)로 진행(조합 순회)
    """
    global min_answer
    if cnt == N // 2:
        # 시너지 계산
        a_total, b_total = get_synergy()
        min_answer = min(min_answer, abs(a_total - b_total))
        return

    for food_number in range(prev + 1, N):
        if visited[food_number]:  # 이미 쓴 재료는 안쓴다.
            continue

        visited[food_number] = 1
        recur(cnt + 1, food_number)
        visited[food_number] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_answer = float('inf')
    recur(0, 0)
    print(f'#{test_case} {min_answer}')