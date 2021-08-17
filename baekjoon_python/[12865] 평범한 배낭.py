# 2021 08 12 다이나믹프로그래밍 배낭 문제
# https://www.acmicpc.net/problem/12865
import sys; input = sys.stdin.readline
n, k = map(int, input().split())
item = []
for i in range(n):
    item.append(tuple(map(int, input().split())))
d = [0]*(k+1)
for i in range(n):
    w, v = item[i]
    m = d[:]
    for j in range(1, k+1):
        if j >= w:
            m[j] = max(v + d[j-w], d[j])
    d = m
print(d[k])
