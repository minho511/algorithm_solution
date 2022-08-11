# type of problem
# https://www.acmicpc.net/problem/2477
import sys; input=sys.stdin.readline
from collections import defaultdict

n = int(input())

data = defaultdict(list)
vt = []
order = []
for i in range(6):
    a, b = map(int, input().split())
    data[a].append((i,b))
    vt.append(b)
w = 1

for i in range(6):
    if len(data[i]) == 1:
        vt[data[i][0][0]-1] = 0
        if data[i][0][0]+1 >= 6:
            vt[0] = 0
        else:
            vt[data[i][0][0]+1] = 0
        w*=data[i][0][1]
t = 1
for i in range(6):
    if vt[i] != 0:
        t*=vt[i]
print((w-t)*n)