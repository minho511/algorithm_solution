import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
p, q = map(int, input().split())
home = list(map(int, input().split()))
store = list(map(int, input().split()))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
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
    return distance


min_dist = INF
min_index = 0
for i in home:
    check_array = dijkstra(i)
    for j in store:
        if check_array[j] < min_dist:
            min_index = i
            min_dist = check_array[j]
print(min_index)