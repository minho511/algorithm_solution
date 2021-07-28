# 2021 07 15 그래프이론 다익스트라
# https://www.acmicpc.net/problem/5972
import sys; input = sys.stdin.readline
import heapq
v, e = map(int, input().split())
INF = int(1e9)
distance = [INF]*(v+1)
graph = [[]for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dikstra(1)
print(distance[v])