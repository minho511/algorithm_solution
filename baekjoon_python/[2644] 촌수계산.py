# https://www.acmicpc.net/problem/2644
from collections import deque
import sys; input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
count = [0]*(n+1)
for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    count[start] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                count[i] = count[x] + 1
                visited[i] = True
bfs(a)
ans = count[b]
if ans == 0:
    print(-1)
else:
    print(count[b])

# 플로이드-워셜 풀이
# import sys; input = sys.stdin.readline
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# INF = int(1e9)
# graph = [[INF]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     c, d = map(int, input().split())
#     graph[c][d] = 1
#     graph[d][c] = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             graph[i][j] = 0
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# ans = graph[a][b]
# if ans == INF or ans == 0:
#     print(-1)
# else:
#     print(ans)