# 2021 08 11 그래프이론 플로이드 워셜
# https://www.acmicpc.net/problem/11404
import sys; input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()