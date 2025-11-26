# 정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    bin_num = bin(M)[2:]
    if bin_num[-N:] == '1' * N:
        print(f'#{test_case}', "ON")
    else:
        print(f'#{test_case}', "OFF")


