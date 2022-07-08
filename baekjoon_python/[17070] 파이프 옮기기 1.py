# 다이나믹 프로그래밍 그래프 이론 그래프 탐색
# https://www.acmicpc.net/problem/17070

import sys; input=sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# b1 = (0,0) b2 = (0, 1)
def state(r1, c1, r2, c2):
    if r2 == r1:
        return 0
    elif c2 == c1:
        return 2
    else:
        return 1
cnt = 0



def dfs(r1, c1, r2, c2):
    global cnt
    # 가로로 놓인 상태로 시작
    s = state(r1, c1, r2, c2)
    if r2 == n-1 and c2 == n-1:
        cnt +=1
        return

    if c2+1 <n and r2+1<n :

        if graph[r2][c2+1]==0 and graph[r2+1][c2+1]==0 and graph[r2+1][c2]==0:
    
            dfs(r2, c2, r2+1, c2+1) 
    if c2+1 <n :
        if  graph[r2][c2+1] == 0:
            if s== 0:
                dfs(r2, c2, r2, c2+1)
            elif s ==1:
                dfs(r2, c2, r2, c2+1)
    if r2+1 < n:
        if graph[r2+1][c2] == 0:
            if s == 1:
                dfs(r2, c2, r2+1, c2)
            elif s == 2:
                dfs(r2, c2, r2+1, c2)
    return    

    
dfs(0,0,0,1)
print(cnt)