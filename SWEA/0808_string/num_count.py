T = int(input())
# str1 = “ABCA”, str2 = “ABABCA”인 경우,
# str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
for test_case in range(1, T+1):
    text1 = list(input())
    text2 = list(input())

    max_cnt = 0  # 가장 많은 글자의 개수
    for i in range(len(text1)):
        cnt = 0  # 각 글자의 개수
        for j in range(len(text2)):
            # 같은 글자가 있으면 개수 +1
            if text1[i] == text2[j]:
                cnt += 1
            # 현재 글자의 개수가 가장 많은 글자보다 많으면 현재 글자 개수 대입
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{test_case} {max_cnt}')

