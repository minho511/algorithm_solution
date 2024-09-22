## 시간 초과..

import sys; input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cnt = 0
q = deque()

n, m = map(int, input().split())
h, w = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
k = int(input())

visit = [[0]*m for _ in range(n)]

for _ in range(k):
    cx, cy = map(int, input().split())
    q.append((cx-1, cy-1))
    
while q:
    cx, cy = q.popleft()
    if visit[cx][cy]: continue
    visit[cx][cy] = 1
    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] >= graph[cx][cy] and not visit[nx][ny]: 
            q.append((nx, ny))

def check(i, j):
    for p in range(i, i+h):
        for q in range(j, j+w):
            if not visit[p][q]: return 0
    return 1

for i in range(n-h+1):
    for j in range(m-w+1):
        cnt += check(i, j)

print(cnt)