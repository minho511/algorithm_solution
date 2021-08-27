# 2021 08 26 그래프 이론 벨만–포드
# https://www.acmicpc.net/problem/11657
import sys; input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = []
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now, next, cost = graph[j]
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == n-1:
                    return True
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])