# 2021 07 09 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    q = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
res = []
mxcnt = 0
for i in range(1, n + 1):
    k = bfs(i)
    if k > mxcnt:
        mxcnt = k
        res = [i]
    elif k == mxcnt:
        res.append(i)
print(*res)