# 2021 07 20 그래프이론 플로이드워셜
# https://www.acmicpc.net/problem/11403
from collections import deque
import sys; input = sys.stdin.readline
n = int(input())
table = []

graph = [[] for _ in range(n)]
for i in range(n):
    k = list(map(int, input().split()))
    table.append(k)
    for j in range(n):
        if k[j] == 1:
            graph[i].append(j)

def bfs(start,visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for i in range(n):
    visited = [False] * n
    if visited[i] is True:
        for l in graph[i]:
            table[i][l] = 1
for i in range(n):
    print(*table[i])