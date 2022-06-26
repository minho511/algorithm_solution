# 구현 그래프 이론 그래프 탐색 너비 우선 탐색 시뮬레이션 깊이 우선 탐색
# https://www.acmicpc.net/problem/2638

import copy
import sys; input=sys.stdin.readline
from collections import deque
N, M  = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    visited = [[False]*M for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    check = []
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in check:
                continue
            if nx <0 or ny <0 or nx >= N or ny>= M:
                continue
            if graph[nx][ny] == 1:
                if visited[nx][ny]:
                    check.append((nx, ny))
                else:
                    visited[nx][ny] = True
            else:
                if visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True
    for x, y in check:
        graph[x][y] = 0
t = 0
while True:
    cnt = 0
    for i in range(N):
        cnt += sum(graph[i])
    if cnt == 0:
        break
    # print(cnt)
    bfs(0, 0)

    t+=1
print(t)