# 나중에 검사해서 id가 두 번 나왔다면, 해당 사람은 건물에 들어왔다가 나간 것이고
# id가 한 번만 나왔다면 해당 사람은 건물에 들어오고 아직 나가지 않은 것



T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # ID 개수
    ID = list(map(int, input().split()))

    ans = 0
    # XOR은 같은 값을 두 번 하면 사라짐
    for i in ID:
        ans ^= i
    print(f'#{test_case} {ans}')

