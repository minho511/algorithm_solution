# 2021 07 14 정렬
# https://www.acmicpc.net/problem/11651
import sys; input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    x,y = map(int, input().split())
    graph.append((y, x))
graph.sort()
for i in range(n):
    print(graph[i][1],graph[i][0])
