# 2021 07 09 구현 그래프이론 그래프탐색 브루트포스 BFS/DFS
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [0,1]
    dy = [1, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            d = graph[x][y]
            nx = x + dx[i]*d
            ny = y + dy[i]*d
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == -1:
                return "HaruHaru"
            if graph[nx][ny] >0:
                queue.append((nx, ny))
    return 'Hing'

print(bfs(0,0))