# 2021 07 17 그래프이론 그래프탐색 깊이우선탐색 플로이드–와샬
# https://www.acmicpc.net/problem/2617
import sys; input = sys.stdin.readline
n, m = map(int, input().split())

graph_h = [[] for _ in range(n+1)]
graph_l = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph_h[a].append(b)
    graph_l[b].append(a)
cnt_h = [0]*(n+1)
cnt_l = [0]*(n+1)

def dfs(graph,v,cnt,visited):
    visited[v] = True
    cnt[v] +=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,cnt,visited)
ans = 0
std = (n+1)//2
for i in range(1, n+1):
    visited_h = [False] * (n + 1)
    visited_l = [False] * (n + 1)
    dfs(graph_h,i,cnt_h,visited_h)
    dfs(graph_l,i,cnt_l,visited_l)
for i in range(1, n+1):
    if cnt_h[i]>std:
        ans+=1
    if cnt_l[i]>std:
        ans+=1
print(ans)

#  플로이드 워셜
# import sys; input = sys.stdin.readline
# n, m = map(int, input().split())
# INF = int(1e9)
# graph = [[INF]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
# for i in range(n+1):
#     for j in range(n+1):
#         if i == j:
#             graph[i][j] = 0
# for k in range(n+1):
#     for i in range(n+1):
#         for j in range(n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# count = [0]*(n+1)
# count2 = [0]*(n+1)
# for j in range(n+1):
#     for i in range(n+1):
#         if graph[i][j] != INF and graph[i][j]!=0:
#             count[i] +=1
#             count2[j] +=1
# std = (n+1)//2
# cnt = 0
# for i in range(n+1):
#     if count[i] >=std:
#         cnt +=1
#     if count2[i] >=std:
#         cnt+=1
# print(cnt)
