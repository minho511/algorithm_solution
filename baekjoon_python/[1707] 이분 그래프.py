# 2021 07 29 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/1707
import sys; input = sys.stdin.readline
from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == visited[x]:
                return False
            if visited[i] == 1-visited[x]:
                continue
            if visited[i] == -1:
                visited[i] = 1-visited[x]
                q.append(i)
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (v + 1)
    res = True
    for i in range(v+1):
        if visited[i] == -1:
            res*=bfs(i)
    if res:
        print("YES")
    else:
        print("NO")