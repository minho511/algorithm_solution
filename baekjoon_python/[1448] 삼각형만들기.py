# 2021 07 10
# https://www.acmicpc.net/problem/1448
import sys
input = sys.stdin.readline
array = []
n = int(input())
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)
res = -1
for i in range(n-2):
    if array[i] < array[i+1]+array[i+2]:
        res = array[i] + array[i+1] + array[i+2]
        break
print(res)