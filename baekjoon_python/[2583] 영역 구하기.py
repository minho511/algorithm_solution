# 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/2583
import sys; input=sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[1]*n for _ in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    cnt = 1
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if nx < 0 or ny < 0 or nx >=m or ny>=n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

cnt = 0
region = []
for x in range(m):
    for y in range(n):
        if graph[x][y] == 1:
            region.append(bfs(x, y))
            cnt += 1
print(cnt)
print(*sorted(region))