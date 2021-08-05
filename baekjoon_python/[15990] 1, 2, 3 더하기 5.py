# 2021 08 05 다이나믹프로그래밍
# https://www.acmicpc.net/problem/15990
import sys; input = sys.stdin.readline
m = 1000000009
d = [[]*3 for i in range(100001)]
d[1] = [1,0,0]
d[2] = [0,1,0]
d[3] = [1,1,1]
for i in range(4,100001):
    d[i]=[(d[i-1][1]+d[i-1][2])%m,(d[i-2][2]+d[i-2][0])%m,(d[i-3][0]+d[i-3][1])%m]
for t in range(int(input())):
    print(sum(d[int(input())])%m)