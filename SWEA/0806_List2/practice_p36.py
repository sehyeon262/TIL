"""
5
GOFFA
OYECR
UABJQ
JAEZN
WJZKC
"""

N = int(input())
text = [input() for _ in range(N)]

# 패턴의 크기
P = 2

pat = ['AB', 'CD']

print(text, pat)

# 패턴이 큰 2차원 배열 사각형 안에 존재하나요? 없다고 가정
answer = 'No'

# 큰 사각형 안에 작은 사각형 영역 만들어서 검사
# 영역 행 좌 표(i
for i in range(N - P + 1):
    for j in range(N - P + 1):

        # (i,j)에서 시작해서 2*2 작은 사각형 영역
        # 큰 사각형 안에 만들 작은 사각형 패턴과 비교할 작은 사각형 패턴이 같다고 가정
        flag = True
        # di(i의 변화량)의 범위 : 0~(p-1)/0에서 작은 패턴의 크기 -1 까지
        # dj(j의 변화량)의 범위 : 0~(p-1)
        # di, dj, 는 작은패턴의 인덱스로도 사용가능
        for di in range(P):
            for dj in range(P):
                if pat[di][dj] != text[i + di][j + dj]:
                    # 하나라도 다르면 패턴 불일치
                    flag = False

        # 비교했는데 아직도 flag = True라면 중간에 False로 바뀌어야한다
        if flag:
            answer = 'Yes'
print(answer)