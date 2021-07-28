# 2021 07 14 브루트포스
# https://www.acmicpc.net/problem/2798
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))
mx= 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if array[i]+array[j]+array[k]>m:
                break
            mx = max(mx, array[i] + array[j] + array[k])
print(mx)