# 2021 07 21 구현 브루트포스 알고리즘
# https://www.acmicpc.net/problem/18111

import sys; input=sys.stdin.readline
n, m, b = map(int, input().split())
graph = []
for _ in range(n):
    graph += list(map(int, input().split()))
time, height = int(1e9), 0
for h in range(0, 257):
    t = 0
    inven = b
    for i in range(n*m):
        if graph[i] == h:
            continue
        elif graph[i] > h:
            t += 2*(graph[i]-h)
            inven += graph[i]-h
        elif graph[i] < h:
            t += h-graph[i]
            inven -= h-graph[i]
    if inven < 0:
        continue
    if t <= time:
        time = t
        if height < h:
            height = h
print(time, height)