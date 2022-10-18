# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/2565
import sys; input=sys.stdin.readline
import sys; input = sys.stdin.readline

n = int(input())
ropes = []
for i in range(n):
    a, b = map(int, input().split())
    ropes.append((a, b))

ropes.sort()
d = [1] * n
for i in range(1,n):
    for j in range(0, i):
        if ropes[i-j-1][1] < ropes[i][1]:
            d[i] = max(d[i-j-1] + 1, d[i])
            
print(n-max(d))