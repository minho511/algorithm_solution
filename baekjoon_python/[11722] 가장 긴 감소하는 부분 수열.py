# 2021 08 10 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/11722
import sys; input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
d = [1]*n
for i in range(1, n):
    for j in range(i):
        if array[j] > array[i]:
            d[i] = max(d[j]+1,d[i])
print(max(d))