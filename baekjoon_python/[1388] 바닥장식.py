# 2021 07 19 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/1388
import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input()[:-1])))

#BFS
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs_a(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 'c'
    while q:
        x, y = q.popleft()
        for i in range(2,4):
            nx = x + dx[i]
            if nx <0 or nx>=n:
                continue
            if graph[nx][y] == '-' or graph[nx][y] == 'c':
                continue
            if graph[nx][y] == '|':
                graph[nx][y] = 'c'
                q.append((nx,y))

def bfs_b(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 'c'
    while q:
        x, y = q.popleft()
        for i in range(2):
            ny = y + dy[i]
            if ny < 0 or x >= n or ny >= m:
                continue
            if graph[x][ny] == '|' or graph[x][ny] == 'c':
                continue
            if graph[x][ny] == '-':
                graph[x][ny] = 'c'
                q.append((x, ny))
cnt_a = 0  # count '|'
cnt_b = 0  # count '-'
for i in range(n):
    for j in range(m):
        if graph[i][j] == '|':
            cnt_a += 1
            bfs_a(i,j)
        if graph[i][j] == '-':
            cnt_b += 1
            bfs_b(i,j)
print(cnt_a+cnt_b)

# bfs를 사용하지 않는 간단한 풀이
# import sys; input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(str, input()[:-1])))
# cnt = n*m
# for i in range(n):
#     for j in range(1,m):
#         if graph[i][j-1] == graph[i][j] == '-':
#             cnt-=1
# for i in range(1,n):
#     for j in range(m):
#         if graph[i-1][j] == graph[i][j] == '|':
#             cnt-=1
# print(cnt)