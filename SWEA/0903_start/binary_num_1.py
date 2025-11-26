# T = int(input())
#
# for test_case in range(1, T+1):
#     N, hexa = input().split()
#
#     binary_num =""
#     # 문자열 -> 16진수
#     hex_num = int(hexa, 16)
#     # 16진수 -> 2진수
#     decimal = bin(hex_num)[2:]
#     # 4자리가 아니면 0을 추가 (N * 4 길이만큼 모자란 0을 추가함)
#     decimal = decimal.zfill(int(N) * 4)
#     binary_num += decimal
#
#     print(f'#{test_case} {binary_num}')

''' 딕셔너리 사용 ------------'''
T = int(input())
for test_case in range(1, T+1):
    N, hexa = input().split()
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    result = ''

    for x in hexa:
        result += hex_to_bin[x]
    print(f'#{test_case} {result}')

