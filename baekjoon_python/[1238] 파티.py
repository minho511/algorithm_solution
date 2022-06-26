# 그래프 이론 데이크스트라
# https://www.acmicpc.net/problem/1238

# 다익스트라 풀이
import heapq
INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for i in range(n+1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    dist = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist

an = [0]*(n+1)
for a in range(1, n+1):
    an[a] += dijkstra(a)[x]
re = dijkstra(x)
for a in range(1, n+1):
    an[a] += re[a]
print(max(an))




# 플로이드 워셜 알고리즘 시간초과
# import sys; input=sys.stdin.readline
# INF = int(1e9)

# N, M, X = map(int, input().split())
# graph = [[INF]*(N+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j:
#             graph[i][j] == 0

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# dist = [0]*(N+1)
# for a in range(1, N+1):
#     dist[a] = graph[X][a] + graph[a][X]
# print(max(dist))