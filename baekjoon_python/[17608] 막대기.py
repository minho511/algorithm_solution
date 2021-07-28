# 2021 07 03 자료구조 스택 구현
import sys
input = sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    stack.append(int(input()))
cnt = 1
std = stack.pop()
while stack:
    k = stack.pop()
    if k > std:
        cnt += 1
        std = k
print(cnt)
