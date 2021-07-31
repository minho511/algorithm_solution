# 2021 07 27 구현 브루트포스 알고리즘
# https://www.acmicpc.net/problem/14500
# PyPy3 제출
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

_mx = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
visited = [[0] * m for _ in range(n)]

def dfs(x,y,sum,cnt):
    global _mx
    if cnt == 4:
        _mx = max(sum,_mx)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny,sum+graph[nx][ny],cnt+1)
            visited[nx][ny] = 0

def another(x,y):
    global _mx
    total = graph[x][y]
    _min = 1001
    check = 0
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<n and 0<=ny<m:
            check += 1
            total += graph[nx][ny]
            if graph[nx][ny] < _min:
                _min = graph[nx][ny]
    if check == 3:
        _mx = max(total, _mx)
    elif check ==4:
        _mx = max(total-_min, _mx)
    return

array = []
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,graph[i][j],1)
        visited[i][j] = 0
        another(i,j)
print(_mx)