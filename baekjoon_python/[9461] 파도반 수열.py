#백준 9461
#2021 06 25
import sys
input = sys.stdin.readline

T = int(input())
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4, 101):
    d[i] = d[i - 2] + d[i - 3]
for _ in range(T):
    print(d[int(input())])

