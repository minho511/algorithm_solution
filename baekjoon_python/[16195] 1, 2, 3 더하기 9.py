# 2021 08 05 다이나믹프로그래밍
# https://www.acmicpc.net/problem/16195
import sys; input = sys.stdin.readline
array = [[0]*1001 for _ in range(1001)]
array[0][0] = 1
for j in range(1, 1001):
    for i in range(1,1001):
        if i == j:
            array[i][j] = 1
        array[j][i] = (array[j-1][i-1]+array[j-2][i-1]+array[j-3][i-1])%1000000009
for _ in range(int(input())):
    n, m = map(int, input().split())
    res = 0
    for i in range(m+1):
        res+=array[n][i]
    sys.stdout.write(str(res%1000000009))
    sys.stdout.write('\n')