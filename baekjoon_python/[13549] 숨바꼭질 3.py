# 2021 08 11 그래프 이론 그래프 탐색 너비 우선 탐색 다익스트라 0-1 너비 우선 탐색
# https://www.acmicpc.net/problem/13549
# 다익스트라 풀이
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
a,b = map(int, input().split())
distance = [INF]*200001

def dijkstra(start,target):
    q = []
    cnt = 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        nx = [(now + 1, 1), (now - 1, 1), (2 * now, 0)]
        for i in nx:
            if i[0]<0 or i[0]>200000:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                if i[0] == target:
                    cnt+=1
                    if cnt >= 3:
                        return distance[target]
                heapq.heappush(q, (cost, i[0]))
    return distance[target]
print(dijkstra(a,b))
