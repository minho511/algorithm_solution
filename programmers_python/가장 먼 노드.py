# 2021 08 18 그래프 level3
# https://programmers.co.kr/learn/courses/30/lessons/49189
import heapq
def solution(n, edge):
    start = 1
    graph = [[] for _ in range(n+1)]
    for data in edge:
        graph[data[0]].append((data[1],1))
        graph[data[1]].append((data[0],1))
    INF = int(1e9)
    q = []
    distance = [-1] + [INF]*(n)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    mx = max(distance)
    answer = distance.count(mx)
    return answer