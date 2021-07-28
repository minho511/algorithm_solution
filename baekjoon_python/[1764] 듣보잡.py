# 2021 07 22 자료구조 문자열 정렬
# https://www.acmicpc.net/problem/1764
from collections import Counter
import sys; input = sys.stdin.readline
d = []
n, m = map(int, input().split())
for _ in range(n+m):
    d.append(input())
cnt = 0
ans = []
for i in sorted(Counter(d).items()):
    if i[1]==2:
        cnt +=1
        ans.append(i[0])
print(cnt)
print("".join(ans))

# 이진탐색을 이용한 풀이
# import sys; input = sys.stdin.readline
# d = []
# ans = []
# n, m = map(int, input().split())
# for _ in range(n):
#     d.append(input())
# d.sort()
# for _ in range(m):
#     s = input()
#     start = 0
#     end = n-1
#     while start<=end:
#         mid = (start+end)//2
#         if d[mid] == s:
#             ans.append(s)
#             break
#         elif s < d[mid]:
#             end = mid-1
#         elif s > d[mid]:
#             start = mid+1
# print(len(ans))
# print("".join(sorted(ans)))