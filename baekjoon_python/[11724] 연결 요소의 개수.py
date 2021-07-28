# 2021 07 22 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/11724
from collections import deque
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(start):
    visited[start] = 1
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt +=1
print(cnt)
