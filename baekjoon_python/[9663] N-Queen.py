# 2021 08 17
# https://www.acmicpc.net/problem/9663



def dfs(y):
    global cnt
    if y == n:
        cnt+=1
        return
    for i in range(n):
        check = True
        for j in range(y):
            if board[j] == i or abs(y-j) == abs(i-board[j]):
                check = False
                break
        if check:
            board[y] = i
            dfs(y+1)

cnt = 0
n = int(input())
board = [0] * n
dfs(0)
print(cnt)