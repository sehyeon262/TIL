# 음이 아닌 정수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소할 때, 그 수를 줄어드는 수라고 한다. 
# 예를 들어, 321와 950은 줄어드는 수이고, 322와 958은 아니다.
# N번째로 작은 줄어드는 수를 출력하는 프로그램을 작성하시오. 
# 만약 그러한 수가 없을 때는 -1을 출력한다. 

# 줄어드는 수들을 작은 것부터 큰 것까지 전부 나열 => 그리고 그 중에서 N번째 수는?

from itertools import combinations

N = int(input())

# 줄어드는 수 저장할 리스트
result = [] 

# 조합 만들자
for length in range(1, 11): # 1 ~ 10
    # 0 ~ 9 숫자 중에 1개, 2개, ..., 10개 뽑기 => 줄어드는 수가 최대 10자리임!(9876543210)
    for comb in combinations(range(10), length):
        sort_num = sorted(comb, reverse=True)
        num = int(''.join(map(str, sort_num)))
        result.append(num)

# 오름차순 정렬
result.sort()

# 원하는 수 출력하자
if N > len(result):
    print(-1)
else:
    print(result[N-1])  # 리스트 인덱스는 0부터 시작하니깐 -1 


    '''
    길이 1 => (0), (1), (2), ...
    길이 2 => (0,1), (0,2), (0,3), ...
    길이 3 => (0,1,2), (0,1,3), (0,1,4), ...

    
    !! 이제 이 조합들을 내림차순으로 붙이자 !!
    ex) comb = (0, 3, 5)
        sorted(comb, reverse=True) => [5, 3, 0] (정수)
    
        
    !! join()은 문자(str) 리스트만 받을 수 있다 !!
    sol) map 활용 -> 하나씩 str로 바꿔주자 => ["5", "3", "0"]

    
    !! 최종 !!
    sol) join -> "530"(str) -> int -> 530 
    
    '''
    