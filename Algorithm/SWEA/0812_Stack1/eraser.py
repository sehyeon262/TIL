T = int(input())

for test_case in range(1, T+1):
    string = list(input())

    i = 0
    while i < len(string) - 1:
        # i번째 위치와 i+1번째 위치가 같으면 삭제
        if string[i] == string[i+1]:
            # 하나 pop하면 앞으로 i가 앞으로 당겨지므로 같은 자리 pop 해야함!!
            string.pop(i)
            string.pop(i)
            # 삭제한 문자열의 앞 뒤가 같을 수 있으므로 -1한 후 새로운 쌍 다시 검사
            if i > 0:
                i -= 1
        # 반복 문자 없으면 +1
        else:
            i += 1
    # 남은 문자열이 없으면 0, 있으면 길이 출력
    result = len(string) if string else 0
    print(f'#{test_case} {result}')

