T = 10

for test_case in range(1, T + 1):
    N, number = input().split()
    N = int(N)
    # 문자열 -> 리스트로 변환 (pop 하기 위해)
    number = list(number)

    i = 0
    # i+1과 비교하므로 마지막 인덱스 바로 전까지 확인해야 함!!
    while i < len(number) - 1:
        # 현재 문자와 다음 문자가 같으면,
        if number[i] == number[i + 1]:
            # 뒤에꺼 먼저 pop => 앞에 먼저 pop 하면 인덱스가 당겨져서 헷갈림
            number.pop(i + 1)
            number.pop(i)
            if i > 0:
                i -= 1
        # 두 문자가 다르면 다음 문자로 넘어감
        else:
            i += 1

    # 리스트 형태로 나오므로 join 사용하여 바꿔줌
    print(f'#{test_case} {"".join(number)}')


