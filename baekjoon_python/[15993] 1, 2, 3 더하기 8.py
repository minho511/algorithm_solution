# 2021 08 05 다이나믹프로그래밍
# https://www.acmicpc.net/problem/15993
import sys; input = sys.stdin.readline
array = [[0,0]for _ in range(100001)]
array[0] = [0,1]
array[1] = [1,0]
array[2] = [1,1]
for i in range(3, 100001):
    array[i][1] = (array[i-1][0]+array[i-2][0]+array[i-3][0])%1000000009
    if i % 4== 0:
        array[i][0] = array[i][1]-1
    elif i%4 == 1:
        array[i][0] = array[i][1]+1
    else:
        array[i][0] = array[i][1]
for _ in range(int(input())):
    n = int(input())
    sys.stdout.write("{} {}\n".format(array[n][0],array[n][1]))