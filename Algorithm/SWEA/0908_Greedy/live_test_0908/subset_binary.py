# 2. 전체 부분 집합을 구할 수 있다.
arr = [1, 2, 3, 4]

# ------ 방식 1 ------
# i : 0~2^n == i번째 부분집합
for i in range(1 << len(arr)):  # 부분집합 번호
    for idx in range(len(arr)):  # 각 원소들을 모두 확인
        # i : 부분집합 번호 (각 자리의 포함 여부)
        # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()

# ------ 방식 2 ------
# 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
def get_sub(tar):
    print(f'target = {tar}', end = '/')
    for i in range(len(arr)):
        # 0x1 로 표기한 이유 (사실 1, 0b1, 0b0001, True 다 가능)
        # - 비트 연산임을 명시하는 권장 방법
        if tar & 0x1:   # 가장 우측 비트를 체크
            print(arr[i], end=' ')
        tar >>= 1

for target in range(1 << len(arr)):
    get_sub(target)
    print()