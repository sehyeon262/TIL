# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_num = ""

    if n == 0:
        return '0'

    while n > 0:
        remain = n % 2
        # 문자열은 reverse 안쓰고 더할 수 있음
        binary_num = str(remain) + binary_num
        n = n // 2

    return binary_num

print(decimal_to_binary(4))
print(bin(4))

# --------------------------------------------------------------
# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hexadecimal_num = ""
    # 변화 X, 조회 => 문자열이 빠름
    # 변화 O, 조회 => 딕셔너리, 리스트
    hex_digits = "0123456789ABCDEF"
    if n == 0:
        return '0'
    
    while n > 0:
        remain = n % 16
        hexadecimal_num = hex_digits[remain] + hexadecimal_num
        n = n // 16

    return hexadecimal_num

print(decimal_to_hexadecimal(17))
print(decimal_to_hexadecimal(31))

# 내장 함수가 있기는 하다! (직접 구현하는 방법을 구하자!)
print(hex(17))
print(hex(31))

# --------------------------------------------------------------
# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0 # 몇 승?

    for digit in reversed(binary_str):
        # 1일 때만 계산해주면 됨
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number

print(binary_to_decimal("11101"))