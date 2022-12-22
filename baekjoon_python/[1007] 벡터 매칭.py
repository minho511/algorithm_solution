# 수학 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1007
import sys; input=sys.stdin.readline
from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    l = range(n)
    points = []
    c = []
    x = 0
    y = 0
    for i in range(n):
        a, b= map(int, input().split())
        points.append([a,b])
        x += a
        y += b
    permu = combinations(l, n//2)
    ans = int(1e11)
    for p in permu:
        nx, ny = x, y
        for i in p:
            tx,ty = points[i]
            nx-=2*tx
            ny-=2*ty
        ans = min(nx**2+ny**2, ans)
    # print(c)
    print(ans**0.5)