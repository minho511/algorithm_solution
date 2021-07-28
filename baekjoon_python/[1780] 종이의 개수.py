# 2021 07 24
# https://www.acmicpc.net/problem/1780
import sys; input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
count = [0,0,0]  # pm1 p0 p1
def seq(n,i,j,target):
    u = True
    cnt = 0
    for p in range(i,i+n):
        for q in range(j,j+n):
            if n == 3 and graph[p][q] == target:
                cnt+=1
            if graph[p][q] != target:
                u = False
    if u:
        count[target] += 1
        return
    if n == 3:
        if cnt==9:
            count[target] +=1
        else:
            count[target] += cnt
        return
    k = n//3
    for p in range(i, i+2*(n//3)+1,n//3):
        for q in range(j, j+2*(n//3)+1,n//3):
            seq(n//3, p, q, target)

seq(n,0,0,-1)
seq(n,0,0,0)
seq(n,0,0,1)

print(f"{count[-1]}\n{count[0]}\n{count[1]}")
