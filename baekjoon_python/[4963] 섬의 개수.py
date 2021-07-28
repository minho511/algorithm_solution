# 2021 07 19 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/4963
import sys
input = sys.stdin.readline
from collections import deque
dx = [-1,-1,-1,0,1,1, 1, 0]
dy = [-1, 0, 1,1,1,0,-1,-1]
def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return graph
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j,graph)
                cnt+=1
    print(cnt)
