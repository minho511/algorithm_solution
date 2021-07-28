# 2021 07 13 자료구조 덱
# https://www.acmicpc.net/problem/10866
from collections import deque
import sys;input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    e = list(map(str, input().split()))
    if e[0] == 'push_front':
        q.appendleft(int(e[1]))
    if e[0] == 'push_back':
        q.append(int(e[1]))
    if e[0] == 'pop_front':
        try:
            print(q.popleft())
        except:
            print(-1)
    if e[0] == 'pop_back':
        try:
            print(q.pop())
        except:
            print(-1)
    if e[0] == 'size':
        print(len(q))
    if e[0] == 'empty':
        print(int(len(q) == 0))
    if e[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    if e[0] == 'back':
        try:
            print(q[-1])
        except:
            print(-1)