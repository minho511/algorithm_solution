# 수학 다이나믹 프로그래밍 조합론
# https://www.acmicpc.net/problem/1256
import sys; input=sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[1]*(n+1)]
for i in range(1, m+1):
    d = [1]
    for j in range(1, n+1):
        d.append(d[j-1]+graph[i-1][j])
    graph.append(d)
if graph[m][n] < k:
    print(-1)
    exit()
ans = ""
x,y = m, n
while x>0 and y>0:
    if k <= graph[x][y-1]:
        ans += 'a'
        y-=1
    else:
        ans += 'z'
        k-=graph[x][y-1]
        x-=1
if x > 0 and y == 0: print(ans+'z'*x)
elif y>0 and x == 0: print(ans+'a'*y)
