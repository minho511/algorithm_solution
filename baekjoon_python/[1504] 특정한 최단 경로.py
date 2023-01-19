# 그래프 이론 데이크스트라
# https://www.acmicpc.net/problem/1504

import sys; input = sys.stdin.readline
from collections import defaultdict
import heapq

INF = int(1e9)
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

start = 1
end = n

def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

start2v = dijkstra(1)
end2v = dijkstra(n)
vv = dijkstra(v1)
ans = min(start2v[v1]+end2v[v2], start2v[v2]+end2v[v1])+vv[v2]
print(-1 if ans >= INF else ans)