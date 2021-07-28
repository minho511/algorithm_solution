# 2021 07 12 다이나믹 프로그래밍 게임 이론
# https://www.acmicpc.net/problem/9657
n = int(input())
d = ["SK"]*1001
d[1] = 1
d[2] = 0
d[3] = 1
d[4] = 1
for i in range(5, n+1):
    d[i] = 1-d[i-1]*d[i-3]*d[i-4]

if d[n] == 1:
    print("SK")
else:
    print("CY")