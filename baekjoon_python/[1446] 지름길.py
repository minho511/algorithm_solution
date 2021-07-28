import sys
import heapq
input = sys.stdin.readline
n, d = map(int, input().split())
graph = [[]for _ in range(d+1)]
for i in range(d):
    graph[i].append((i+1, 1))
for _ in range(n):
    x, y, z = map(int, input().split())
    if y > d:
        continue
    graph[x].append((y, z))
INF = int(1e9)
distance = [INF for i in range(d+1)]
q = []
heapq.heappush(q, (0, 0))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[d])
