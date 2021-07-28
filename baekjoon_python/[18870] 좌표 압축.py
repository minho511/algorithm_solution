# 2021 07 17 정렬 값/좌표압축
# https://www.acmicpc.net/problem/18870
import sys; input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
k = sorted(set(array))
m = {}
for i in range(len(k)):
    m[k[i]] = i
for i in array:
    print(m[i],end=" ")