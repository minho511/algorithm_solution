# 2021 07 19 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/7576
from collections import deque
import sys; input = sys.stdin.readline
m, n = map(int, input().split())
graph = []
tomato = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i,j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = -1
while tomato:
    cnt +=1
    for _ in range(len(tomato)):
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                tomato.append((nx,ny))
for i in graph:
    if 0 in i:
        print(-1)
        exit(0)
print(cnt)