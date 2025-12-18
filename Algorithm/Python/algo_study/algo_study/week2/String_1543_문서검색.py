s = list(input())  # 문자열
p = list(input())  # 검색하고 싶은 단어

i = 0
cnt = 0

while i <= len(s) - len(p):
    # 글자가 같으면
    if s[i:i+len(p)] == p:
        cnt += 1
        # 패턴 길이 만큼 같으므로 길이만큼 점프해줌
        i += len(p)
    # 글자가 다르면
    else:
        # 한 글자만 이동
        i += 1
print(cnt)
