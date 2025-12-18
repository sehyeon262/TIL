# 모든 무게 추를 양팔저울 위에 올리는 순서는 총 N!가지가 있고,
# 오른쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 더 커져서는 안 된다.
# ==> 오른쪽 총합 <= 왼쪽 무게의 총합

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))
    
    print(f)