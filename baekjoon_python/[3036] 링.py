# 수학 정수론 유클리드 호제법
# https://www.acmicpc.net/problem/3036
import sys; input=sys.stdin.readline

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

n = int(input())
r = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(r[i],r[0])
    print(f"{r[0]//g}/{r[i]//g}")
    