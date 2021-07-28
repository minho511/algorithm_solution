# 다익스트라 2021 07 02
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))         # 모든 노드 사이의 거리 1


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)
cnt = 0
for i in range(n+1):
    if distance[i] == k:  # 최단 거리가 K인 도시번호를 오름차순으로 출력한다.
        print(i)
        cnt += 1
if cnt == 0:        # 거리가 K인 도시가 존재하지 않을때
    print(-1)
