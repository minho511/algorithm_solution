import sys; input = sys.stdin.readline
from collections import deque

dx = [-1, -2, +1, +2, -1, -2, +1, +2]
dy = [-2, -1, -2, -1, +2, +1, +2, +1]

for _ in range(int(input())):
    n = int(input())
    visit = [[0]*n for _ in range(n)]
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())

    visit[cx][cy] = 1
    q = deque([(cx, cy)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n: continue
            if visit[nx][ny]>0: continue
            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
            if nx == tx and ny == ty:
                break
    print(visit[tx][ty]-1)

        