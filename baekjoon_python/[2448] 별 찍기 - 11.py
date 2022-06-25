# 재귀
# https://www.acmicpc.net/problem/2448
import sys; input=sys.stdin.readline

n = int(input())

star = [[" "]*(2*n) for _ in range(n)]


def draw(n,m):
    star[n][m] = "*"
    star[n+1][m-1] = "*"
    star[n+1][m+1] = "*"
    star[n+2][m-2] = "*"
    star[n+2][m-1] = "*"
    star[n+2][m+2] = "*"
    star[n+2][m+1] = "*"
    star[n+2][m] = "*"

draw(0, n-1)
if n > 3:
    for i in range(3, n,3):
        for j in range(1,2*n):

            if star[i-1][j-1] == " " and star[i-1][j] == "*":
                if star[i-1][j-2] == "*":
                    continue
                draw(i, j-1)
            elif star[i-1][j-1] == "*" and star[i-1][j] == " ":
                if star[i-1][j+1] == "*":
                    continue
                draw(i, j)
        

for i in range(n):
    for j in range(2*n):
        print(star[i][j], end="")
    print()
