# 2021 08 07 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1149
import sys; input = sys.stdin.readline
n = int(input())
r,g,b = map(int, input().split())
dr = [r]
dg = [g]
db = [b]
for i in range(1, n):
    r, g, b = map(int, input().split())
    dr.append(min(dg[i-1], db[i-1])+r)
    dg.append(min(dr[i-1], db[i-1])+g)
    db.append(min(dr[i-1], dg[i-1])+b)
print(min(dr[n-1],dg[n-1],db[n-1]))
