#백준 2579
import sys
input = sys.stdin.readline

step = []
dpt = []

n = int(input())
for _ in range(n):
    step.append(int(input()))

dpt.append(step[0])
dpt.append(max(step[0] + step[1], step[1]))
dpt.append(max(step[0] + step[2], step[1] + step[2]))
for i in range(4, n):
    dpt.append(max(dpt[i-2] + step[i], dpt[i-3] + step[i] + step[i-1]))
print(dpt.pop())

