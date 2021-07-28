# 2021 07 09 그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt +=1
    print(cnt)

