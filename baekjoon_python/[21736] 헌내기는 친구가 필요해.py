# type of problem
# link
import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    s = input().rstrip()
    for j in range(len(s)):
        if s[j] == 'I':
            x, y = i, j
    graph.append(list(s))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
q = deque([(x, y)])
graph[x][y] = '?'
while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx = cx+dx[i]
        ny = cy+dy[i]
        if nx < 0 or nx >= n or ny<0 or ny>=m: continue
        if graph[nx][ny] == '?' or graph[nx][ny] == 'X': continue
        if graph[nx][ny] == 'P':
            result+=1
        graph[nx][ny] = '?'
        q.append((nx, ny))

print(result if result> 0 else 'TT')
