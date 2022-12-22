# 자료 구조 큐
# https://www.acmicpc.net/problem/15828
import sys; input=sys.stdin.readline
from collections import deque

buffer = deque(list())
n = int(input())
while True:
    inp=int(input())
    if inp == -1:
        break
    elif inp == 0:
        buffer.popleft()
    else:
        if len(buffer) == n:
            continue
        buffer.append(inp)
if buffer:
    print(*buffer)
else:
    print('empty')
