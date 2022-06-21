# 수학 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/2225
import sys; input=sys.stdin.readline
N, K = map(int, input().split())

d = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    d[i][1] = 1
for j in range(1,K+1):
    d[1][j] = j
for i in range(2,N+1):
    for j in range(2,K+1):
        d[i][j] = d[i-1][j]+d[i][j-1]
print(d[N][K]%1000000000)
