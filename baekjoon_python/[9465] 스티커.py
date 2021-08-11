# 2021 08 11 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9465
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    array = []
    if n == 1:
        n1 = int(input())
        n2 = int(input())
        print(max(n1, n2))
    else:
        for i in range(2):
            array.append(list(map(int, input().split())))
        d0 = [array[0][0],array[1][0]+array[0][1]]
        d1 = [array[1][0],array[1][1]+array[0][0]]
        for i in range(2, n):
            d0.append(array[0][i]+max(d1[i-1], d1[i-2]))
            d1.append(array[1][i]+max(d0[i-1], d0[i-2]))
        print(max(d0[n-1], d1[n-1]))