# 구현 문자열
# https://www.acmicpc.net/problem/7567
import sys; input=sys.stdin.readline().rstrip

b = list(input())

cur = b[0]
ans = 10
for c in b[1:]:
    if c == cur:
        ans += 5
    else:
        ans += 10
        cur = c

print(ans)