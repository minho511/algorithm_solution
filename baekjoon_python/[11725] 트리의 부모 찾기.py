# 2021 08 10 그래프 이론 그래프 탐색 트리 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/11725
import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph=[[] for _ in range(n+1)]
parent = [0]*(n+1)
for i in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)]

def bfs(root):
    q = deque([root])
    visited[root] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                parent[i] = x
                visited[i] = True
                q.append(i)
bfs(1)
for i in range(2, n+1):
    print(parent[i])