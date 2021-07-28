# 2021 07 23
# https://www.acmicpc.net/problem/2630
import sys; input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
count = [0,0]

def seq(n,i,j):
    if n == 1:
        if graph[i][j] == 1:
            count[1] += 1
        elif graph[i][j] == 0:
            count[0] += 1
        return
    checkblue = True
    checkwhite = True
    for p in range(i,i+n):
        for q in range(j,j+n):
            if graph[p][q] != 1:
                checkblue = False
            elif graph[p][q] != 0:
                checkwhite = False
    if checkblue:
        count[1] += 1
        return
    elif checkwhite:
        count[0] += 1
        return
    seq(n//2,i,j)
    seq(n//2,i+n//2,j)
    seq(n//2,i,j+n//2)
    seq(n//2,i+n//2,j+n//2)

seq(n,0,0)
print(count[0])
print(count[1])