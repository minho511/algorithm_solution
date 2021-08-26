# 2021 08 26 그래프 이론 벨만–포드
# https://www.acmicpc.net/problem/1865
import sys; input = sys.stdin.readline
INF = sys.maxsize

def bf():
    for i in range(n):
        for j in range(2*m+w):
            node, next_node, cost = graph[j]
            if distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node] + cost
                if i == n-1:
                    return True
    return False

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s,e,-t))
    distance = [INF for _ in range(n+1)]
    print("YES" if bf() else "NO")
