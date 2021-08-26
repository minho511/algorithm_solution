# 2021 08 25 그래프 이론 그래프 탐색 트리 깊이 우선 탐색
# https://www.acmicpc.net/problem/1167
import sys; input = sys.stdin.readline
import heapq
v = int(input())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(v):
    data = list(map(int,input().split()))
    node = data[0]
    for j in range(1,len(data)-1):
        if j%2 == 1:
            nnode = data[j]
        else:
            dist = data[j]
            graph[node].append((nnode, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
mx = max(distance[1:])
p1 = distance.index(mx)
distance = [INF]*(v+1)
dijkstra(p1)
print(max(distance[1:]))