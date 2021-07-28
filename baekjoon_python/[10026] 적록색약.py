# 2021 07 25 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/10026
import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input()[:-1])))
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs_1(x,y):   # 적록색약이 아닌 사람이 보는 그림
    q = deque()
    std = 'c'
    target = graph[x][y]
    if target == 'B':   # 이후 적록색약이 보는 그림이 필요하므로 B와 R,G는 구분하여 방문처리
        std = 'k'
    q.append((x,y))
    graph[x][y] = std
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny <0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == target:
                graph[nx][ny] = std
                q.append((nx,ny))

def bfs_2(x,y):  # 적록색약이 보는 그림 bfs_1실행 이후 얻은 graph
    q = deque()
    target = graph[x][y]
    q.append((x,y))
    graph[x][y] = 'p'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny <0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == target:
                graph[nx][ny] = 'p'
                q.append((nx,ny))

cnt = 0
cnt1 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 'c' and graph[i][j] != 'k':
            cnt+=1
            bfs_1(i,j)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 'p':
            cnt1+=1
            bfs_2(i,j)
print(cnt,cnt1)