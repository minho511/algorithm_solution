# 2021 08 18 그래프이론 다익스트라
# https://www.acmicpc.net/problem/17396
import heapq
import sys; input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
see = list(map(int, input().split()))
see[-1] = 0
graph = [[] for _ in range(n)]
distance = [INF]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    if see[a] == 1 or see[b] == 1:
        continue
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(0)
ans = distance[n-1]
if ans == INF:
    print(-1)
else:
    print(ans)