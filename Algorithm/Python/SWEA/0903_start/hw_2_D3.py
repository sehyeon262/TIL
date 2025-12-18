# 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.
#  ex) 암호코드가 88012346일 경우,
#  ((8 + 0 + 2 + 4) x 3) + (8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.

# 주어진 암호코드가 올바른 암호코드일 경우, 암호코드에 포함된 숫자의 합을 출력하라. 만약 잘못된 암호코드일 경우 대신 0을 출력하라.

# 암호가 있는 위치 찾는 함수
# 암호 비트들은 오른쪽이 다 1로 시작 => 오른쪽 끝부터 '1' 찾기
def start_find(arr):
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                return i, j

def code(code_map, arr, x, y):
    lst = []    # 계산 할 리스트
    # 7개씩 잘라서 code_map에 맞는 값 찾음 => int로 변환해서 lst에 저장
    for k in range(y-55, y+1, 7):
        seg = code_map[''.join(arr[x][k:k+7])]
        lst.append(int(seg))

    even_v = 0
    odd_v = 0
    # 인덱스는 0부터 시작하므로 '(짝수 인덱스 합) * 3 + (홀수 인덱스 합) 으로 계산'
    for i in range(len(lst)):
        if i % 2 == 0:
            even_v += lst[i]
        else:
            odd_v += lst[i]

    result = even_v * 3 + odd_v
    if result % 10 == 0:
        return sum(lst)
    else:
        return 0


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    code_map = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9',
    }

    x, y = start_find(arr)
    ans = code(code_map, arr, x, y)
    print(f'#{test_case} {ans}')
