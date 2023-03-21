# type of problem
# link
import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = []

def check_candi(x, y):
    
    if x == 0 and 0 < y < m-1:
        if graph[x+1][y-1] == 1 or graph[x+1][y+1] == 1:
            return True
    elif x == n-1 and 0<y<m-1:
        if graph[x-1][y-1] == 1 or graph[x-1][y+1] == 1:
            return True
    elif y == 0 and 0<x<n-1:
        if graph[x-1][y+1] == 1 or graph[x+1][y+1] == 1:
            return True
    elif y == m-1 and 0<x<n-1:
        if graph[x-1][y-1] == 1 or graph[x+1][y-1] == 1:
            return True
    elif x == 0 and y == 0:
        if graph[x+1][y] == 1 and graph[x][y+1]==1:
            return True
    elif x == n-1 and y == 0:
        if graph[x-1][y] == 1 and graph[x][y+1]==1:
            return True
    elif x == n-1 and y == m-1:
        if graph[x-1][y] == 1 and graph[x][y-1]==1:
            return True
    elif x == 0 and y == m-1:
        if graph[x+1][y] ==1 and graph[x][y-1] == 1:
            return True
    else:
        if (graph[x-1][y-1] + graph[x+1][y-1] + graph[x-1][y+1] + graph[x+1][y+1]) >=2:
            return True
    return False
    
def bfs(x, y):
    q = deque([(x, y)])
    dist = [[0]*m for _ in range(n)]
    dist[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if dist[nx][ny] != 0:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[cx][cy] + 1        
            if check_candi(nx, ny):
                check.append((nx, ny, dist[nx][ny]))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            print(check)