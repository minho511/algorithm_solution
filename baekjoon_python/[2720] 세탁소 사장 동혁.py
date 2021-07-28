# 2021 07 06 그리디
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    c = int(input())
    q = c//25
    c -= q*25
    d = c//10
    c -= d * 10
    n = c//5
    p = c - n*5
    print(q,d,n,p)