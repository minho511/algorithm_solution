# 2021 07 17 자료구조 큐2
# https://www.acmicpc.net/problem/18258
from collections import deque
import sys; input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    s = input().rstrip()
    l = len(q)
    if s[:4] == 'push':
        a= s.split()[1]
        q.append(int(a))
    elif s == 'pop':
        if l == 0:
            print(-1)
            continue
        print(q.popleft())
    elif s == 'size':
        print(l)
    elif s == 'empty':
        if l == 0:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if l == 0:
            print(-1)
            continue
        print(q[0])
    elif s == 'back':
        if l == 0:
            print(-1)
            continue
        print(q[-1])