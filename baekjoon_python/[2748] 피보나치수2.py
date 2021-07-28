import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 91
d[0] = 1
d[1] = 1
for i in range(n-2):
    d[i+2] = d[i] + d[i+1]
print(d[n-1])
