# T = int(input())
# # 양의 정수가 주어졌을때 해당 정수의 1로 설정된 비트의 개수를 구하시오
#
# for test_case in range(1, T+1):
#     num = int(input())
#     binary_num = bin(num)[2:]
#     cnt = 0
#     for x in binary_num:
#         if x == '1':
#             cnt += 1
#     print(f'#{test_case} {cnt}')

T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    cnt = 0
    while num:
        # 최하위 비트가 1인가?
        cnt += num & 1
        # 오른쪽으로 한칸 이동 (ex. 1101 >> 1 => 110)
        num >>= 1
    print(f'#{test_case} {cnt}')

