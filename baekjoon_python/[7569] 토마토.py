# 2021 07 29 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/7569
import sys; input = sys.stdin.readline
from collections import deque
m, n, t = map(int, input().split())
graph = [[[]for _ in range(n)] for _ in range(t)]
tomato = deque()
cntz = 0
for j in range(t):
    for i in range(n):
        graph[j][i]=list(map(int, input().split()))
        for k in range(m):
            if graph[j][i][k] == 1:
                tomato.append((j,i,k))
            elif graph[j][i][k] == 0:
                cntz += 1
dh = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
cnt = -1
while tomato:
    cnt+=1
    for _ in range(len(tomato)):
        h,x,y = tomato.popleft()
        for i in range(6):
            nh = h+dh[i]
            nx = x+dx[i]
            ny = y+dy[i]
            if nh<0 or nh>= t or nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nh][nx][ny] == -1:
                continue
            if graph[nh][nx][ny] == 0:
                cntz-=1
                graph[nh][nx][ny] = 1
                tomato.append((nh,nx,ny))
if cntz>0:
    print(-1)
else:
    print(cnt)