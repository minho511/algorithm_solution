# 2021 07 15 그래프 이론 그래프 탐색 너비 우선 탐색 다익스트라
# https://www.acmicpc.net/problem/14496
import sys; input = sys.stdin.readline
import heapq
s, end = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # a에서 1의 비용으로 b 치환
    graph[b].append((a, 1))
def dikstra(start, end):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]
result = dikstra(s,end)
if result == INF:
    print(-1)
else:
    print(result)
