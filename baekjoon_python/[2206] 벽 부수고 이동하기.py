# 2021 08 18 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/2206
import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = []
distance = [[[0, 0] for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input()[:-1])))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
distance[0][0][0] = 1
q = deque([(0,0,0)])
while q:
    x, y, check = q.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or ny <0 or nx>=n or ny>=m:
            continue
        if graph[nx][ny] == 1 and not check and distance[nx][ny][1] == 0:
            q.append((nx, ny, 1))
            distance[nx][ny][1] = distance[x][y][0]+1
        elif graph[nx][ny] == 0 and distance[nx][ny][check] == 0:
            distance[nx][ny][check] = distance[x][y][check] + 1
            q.append((nx, ny, check))
a1, a2 = distance[-1][-1]
if a1+a2 == 0:
    print(-1)
elif a1 == 0:
    print(a2)
elif a2 == 0:
    print(a1)
else:
    print(min(a1, a2))