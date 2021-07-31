# 2021 07 31 분할 정복 재귀
# https://www.acmicpc.net/problem/1992
import sys; input=sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def quardTree(x,y,n):
    if n == 1:
        print(graph[x][y],end="")
        return
    check0 = True
    check1 = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] == 1:
                check0 = False
            elif graph[i][j] == 0:
                check1 = False
    if check0:
        print(0, end="")
        graph[x][y] = -1
        return 0
    elif check1:
        print(1, end="")
        graph[x][y] = -1
        return 1
    else:
        print('(',end="")
        quardTree(x,y,n//2)
        quardTree(x,y+n//2,n//2)
        quardTree(x+n//2,y,n//2)
        quardTree(x+n//2,y+n//2,n//2)
        print(')',end="")


quardTree(0,0,n)