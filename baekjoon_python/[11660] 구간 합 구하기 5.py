# 2021 08 08 다이나믹 프로그래밍 누적합
# https://www.acmicpc.net/problem/11660
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0]*(n+1)]
t = [0]*(n+1)
for i in range(n):
    k = [0]+list(map(int, input().split()))
    s = 0
    for j in range(n+1):
        s += k[j]
        k[j] = s
        t[j] += k[j]
    p = t[:]
    graph.append(p)
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sys.stdout.write("{}\n".format(graph[x2][y2]-graph[x1-1][y2]-graph[x2][y1-1]+graph[x1-1][y1-1]))