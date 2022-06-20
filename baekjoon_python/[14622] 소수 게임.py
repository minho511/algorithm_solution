# 수학 구현 자료구조 정수론 우선순위큐 소수판정 에라토스테네스의 체
# https://www.acmicpc.net/problem/14622
import sys; input=sys.stdin.readline

# 에라토스테네스의 체
n = 5000000
sieve = [True] * n
sieve[0] = False
sieve[1] = False
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, n, i):
            sieve[j] = False
check = sieve.copy()
N = int(input())
p1_score, p2_score = 0, 0
p1_called, p2_called = [], []

for _ in range(N):
    p1, p2 = map(int, input().split())
    # p1 대웅
    if sieve[p1]: # 소수라면
        if check[p1]: # 소수이고 처음 나오는 수이면
            check[p1] = False
            p1_called.append(p1)
            p1_called.sort(reverse=True)
            if len(p1_called) == 4:
                p1_called.pop()
        else: # 소수이지만 앞에 나왔던 수이면
            p1_score -= 1000
    else: # 소수가 아니면
        p2_score += p2_called[2] if len(p2_called) == 3 else 1000
    # p2 규성
    if sieve[p2]: # 소수라면
        if check[p2]: # 소수이고 처음 나오는 수이면
            check[p2] = False
            p2_called.append(p2)
            p2_called.sort(reverse=True)
            if len(p2_called) == 4:
                p2_called.pop()
        else: # 소수이지만 앞에 나왔던 수이면
            p2_score -= 1000
    else: # 소수가 아니면
        p1_score += p1_called[2] if len(p1_called) == 3 else 1000
if p1_score > p2_score:
    print("소수의 신 갓대웅")
elif p1_score < p2_score:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")

# heap을 사용한 풀이 (효율은 비슷하다)
# import sys; input=sys.stdin.readline
# import heapq
# # 에라토스테네스의 체
# n = 5000000
# sieve = [True] * n
# sieve[0] = False
# sieve[1] = False
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:
#         for j in range(i+i, n, i):
#             sieve[j] = False
# check = sieve.copy()
# N = int(input())
# p1_score, p2_score = 0, 0
# p1_called, p2_called = [], []

# for _ in range(N):
#     p1, p2 = map(int, input().split())
#     # p1 대웅
#     if sieve[p1]: # 소수라면
#         if check[p1]: # 소수이고 처음 나오는 수이면
#             check[p1] = False
#             heapq.heappush(p1_called, (-p1, p1))
#         else: # 소수이지만 앞에 나왔던 수이면
#             p1_score -= 1000
#     else: # 소수가 아니면
#         temp = []
#         point = 0
#         if len(p2_called) < 3:
#             p2_score += 1000
#         else:
#             for i in range(3):
#                 a, point = heapq.heappop(p2_called)
#                 heapq.heappush(temp, (a,point))
#             p2_called = temp
#             p2_score += point
#     # p2 규성
#     if sieve[p2]: # 소수라면
#         if check[p2]: # 소수이고 처음 나오는 수이면
#             check[p2] = False
#             heapq.heappush(p2_called, (-p2, p2))
#         else: # 소수이지만 앞에 나왔던 수이면
#             p2_score -= 1000
#     else: # 소수가 아니면
#         temp = []
#         point = 0
#         if len(p1_called) < 3:
#             p1_score += 1000
#         else:
#             for i in range(3):
#                 a, point = heapq.heappop(p1_called)
#                 heapq.heappush(temp, (a,point))
#             p1_called = temp
#             p1_score += point

# if p1_score > p2_score:
#     print("소수의 신 갓대웅")
# elif p1_score < p2_score:
#     print("소수 마스터 갓규성")
# else:
#     print("우열을 가릴 수 없음")