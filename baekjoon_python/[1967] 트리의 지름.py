# 2021 08 22 그래프 이론 그래프 탐색 트리 깊이 우선 탐색
# https://www.acmicpc.net/problem/1967
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start, cost):
    for i in graph[start]:
        d = cost+i[1]
        if distance[i[0]] == -1:
            distance[i[0]] = d
            dfs(i[0], d)

# 루트에서 가장 먼 점 찾기 p1
distance = [-1]*(n+1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
# p1에서 가장 먼 점 찾기 p2
distance = [-1]*(n+1)
distance[start] = 0
dfs(start, 0)
# p1 과 p2의 거리가 지름
print(max(distance))