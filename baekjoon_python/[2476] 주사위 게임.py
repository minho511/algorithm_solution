# 수학 구현
# https://www.acmicpc.net/problem/2476
import sys; input=sys.stdin.readline


ps = []
for _ in range(int(input())):
    a, b, c= map(int, input().split())
    if a == b == c:
        p = 10000+a*1000
    elif a == b or b == c:
        p = 1000 + b*100
    elif a == c:
        p = 1000 + a*100
    else:
        p = max([a,b, c])*100
    ps.append(p)
print(max(ps))
