# 2021 07 10 정렬
# https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
array.sort()
for i in array:
    print(*i)