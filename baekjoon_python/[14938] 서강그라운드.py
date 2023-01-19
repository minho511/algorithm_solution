# 그래프 이론 데이크스트라 플로이드–워셜
# https://www.acmicpc.net/problem/14938

import sys; input = sys.stdin.readline

n, m, r = map(int, input().split())
tems = [0]+list(map(int, input().split()))
INF = int(1e9)

distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    distance[b][a] = c
    
res = [0]*(n+1)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][k]+distance[k][j], distance[i][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] != INF and distance[i][j]<=m:
            res[i]+=tems[j]
print(max(res))