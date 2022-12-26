# 수학 구현 사칙연산
# https://www.acmicpc.net/problem/25341
import sys; input=sys.stdin.readline

n, m, q=  map(int, input().split())
info = []
for _ in range(m):
    x = list(map(int, input().split()))
    info.append(x)

oper = [0]*n
W_fc = list(map(int, input().split()))
B = 0
for i in range(m):
    b = info[i][-1]
    c = info[i][0]
    w = info[i][1+c: 1+2*c]
    p = info[i][1:1+c]
    B += b*W_fc[i]
    for j in range(c):
        oper[p[j]-1] += (w[j]* W_fc[i])

for _ in range(q):
    inp = list(map(int, input().split()))
    ans = W_fc[-1]
    for i in range(n):
        ans+=inp[i]*oper[i]
        
    print(ans+B)