def reverse(string):

    # string의 맨 두에서부터 글자 하나씩 떼어와서 result에 붙이면 된다
    for i in range(len(string)-1,-1,-1):
        # string의 i번 인덱스에 있는 글자를 result에 붙이기
        result += string[i]

    return result

s = 'Rverse this string'
