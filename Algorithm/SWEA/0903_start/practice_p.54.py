# 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기
bit = '00000010001101'
N = len(bit)

for i in range(0, N, 7):
    # i번 비트에서 7칸 잘라서 십진수로 만들고 출력
    ith_bin = bit[i:i+7]

    # 십진수로 바꾸기
    decimal = 0

    for j in range(6, -1, -1):
        decimal += int(ith_bin[j]) * 2 ** (6-j)

    print(decimal)


