# 수학 그리디 알고리즘 정렬
# https://www.acmicpc.net/problem/2217
import sys; input=sys.stdin.readline
n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))
ropes.sort()
maxw = 0
for i in range(n):
    w = ropes[i]*(n-i)
    if w > maxw:
        maxw =w
print(maxw)