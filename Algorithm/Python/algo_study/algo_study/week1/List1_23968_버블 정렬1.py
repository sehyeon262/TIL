# N(5<=N<=10000) : 배열 A의 크기, K(1<=K<=N**2) : 교환 횟수
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 조건
# k번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력
# 교환 횟수가 k보다 작으면 -1 출력
change_count = 0
change_num = []
for i in range(N-1, 0, -1):  # ex)N=5 -> i = 4, 3, 2, 1
    for j in range(i):
          # j = 0-4, 
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            change_count += 1
            if change_count == K:
                change_num.append(arr[j])
                change_num.append(arr[j + 1])
                change_num.sort()  # 작은 수부터 정렬

if change_count < K:
    print(-1)
else:
    print(f'{change_num[0]} {change_num[1]}')
    
    
