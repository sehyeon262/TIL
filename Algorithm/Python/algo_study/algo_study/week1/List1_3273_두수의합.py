n = int(input())  # 수열의 크기
seq = list(map(int, input().split()))  # 수열에 포함되는 수
x = int(input())

# 시간 복잡도
# 반복문: O(N^2)

# count = 0  # 쌍의 수
# for i in range(n-1):
#     for j in range(i+1, n):
#         if seq[i] + seq[j] == x:
#             count += 1                
# print(count)


# 시간 복잡도
# 반복문: O(n)
# set 탐색: O(1)
# => 총 O(n)

seen = set()   # 지금까지 본 숫자 저장 => set은
count = 0

# 현재 숫자 num과 더해서 x가 되는 짝이 이미 전에 나왔는지 확인
# 나왔다면, 이미 전에 읽은 숫자 중에 짝이 있다는 의미
for num in seq:
    if (x - num) in seen:
        count += 1  
    seen.add(num)

print(count)