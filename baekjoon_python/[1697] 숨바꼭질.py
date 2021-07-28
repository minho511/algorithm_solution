# 2021 07 23 그래프이론 그래프탐색 너비우선탐색
# https://www.acmicpc.net/problem/1697
from collections import deque
n, k = map(int, input().split())
graph = [[]for _ in range(100001)]
visited = [0]*100001
for i in range(0, 100001):
    graph[i]=[i+1,i-1,2*i]

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]-1
        for nx in graph[x]:
            if nx <0 or nx>100000:
                continue
            if visited[nx] != 0:
                continue
            q.append(nx)
            visited[nx] = visited[x]+1

print(bfs(n))