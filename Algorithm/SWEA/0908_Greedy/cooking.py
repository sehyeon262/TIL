# 입력: N (짝수), S[N][N]
# pair[i][j] = S[i][j] + S[j][i]  // i<j만 유효
#
# best = +∞
# chosen = [False]*N
# chosen[0] = True                 // 대칭 제거 (0은 A에 고정)
#
# recur(start, picked_cnt, sumA):
#     if picked_cnt == N/2:        // A 완성
#         // B 합 계산
#         sumB = 0
#         for i<j:
#             if !chosen[i] and !chosen[j]:
#                 sumB += pair[i][j]
#         best = min(best, |sumA - sumB|)
#         return
#
#     for i from start to N-1:
#         if not chosen[i]:
#             // i를 A에 넣을 때 추가될 시너지 계산
#             add = 0
#             for p in range(N):
#                 if chosen[p] and p<i:
#                     add += pair[p][i]
#                 if chosen[p] and i<p:
#                     add += pair[i][p]  // 구현상 i<j만 쓰면 분기 없어짐
#
#             chosen[i] = True
#             recur(i+1, picked_cnt+1, sumA + add)
#             chosen[i] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

