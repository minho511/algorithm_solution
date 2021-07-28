# 2021 07 12 수학 다이나믹 프로그래밍 조합론
# https://www.acmicpc.net/problem/1010
import sys
input = sys.stdin.readline
d = [0]*30
d[0] = 1
d[1] = 1
for i in range(2, 30):
    d[i] = d[i-1] * i
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    res = d[m]//(d[n]*d[m-n])
    print(res)