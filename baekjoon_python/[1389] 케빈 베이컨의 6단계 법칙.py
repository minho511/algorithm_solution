# 2021 07 27 그래프 이론 그래프 탐색 너비 우선 탐색 플로이드–와샬
# https://www.acmicpc.net/problem/1389
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
res = [0]*(n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i] += graph[i][j]
_mindex = 0
std = INF
for i in range(1,n+1):
    if res[i]<std:
        std = res[i]
        _mindex = i
print(_mindex)