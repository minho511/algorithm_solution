# type of problem
# https://www.acmicpc.net/problem/15681
import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] += 1
    for p in graph[x]:
        if visited[p]==0:
            visited[x]+=dfs(p)
    return visited[x]

dfs(r)

for _ in range(q):
    q_ = int(input())
    print(visited[q_])