# 그래프 이론 데이크스트라
# https://www.acmicpc.net/problem/11779
import sys; input=sys.stdin.readline
import heapq
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [[INF,""] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start][0] = 0
distance[start][1] = str(start)
while q:
    dist, now = heapq.heappop(q)
    if distance[now][0] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]][0]:
            distance[i[0]][0] = cost
            distance[i[0]][1] = distance[now][1] + " " + str(i[0])
            heapq.heappush(q, (cost, i[0]))
print(distance[end][0])
print(len(distance[end][1].split()))
print(distance[end][1])
