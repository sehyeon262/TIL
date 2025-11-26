T = int(input())

for tc in range(1, T+1):
    # N: 테스트케이스 개수
    test_case, N = input().split()
    arr = input().split()

    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = []
    for num in numbers:
        for i in range(int(N)):
            if arr[i] == num:
                result.append(arr[i])

    print(f'{test_case}')
    print(*result)





