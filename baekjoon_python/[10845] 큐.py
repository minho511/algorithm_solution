# 2021 07 14
# https://www.acmicpc.net/problem/10845
import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque()
for _ in range(n):
    s = list(map(str,input().split()))
    k = s[0]
    if k == "push":
        q.append(int(s[1]))
    elif k == "pop":
        try:
            print(q.popleft())
        except:
            print(-1)
    elif k == "size":
        print(len(q))
    elif k == "empty":
        print(int(len(q) == 0))
    elif k == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif k == "back":
        try:
            print(q[-1])
        except:
            print(-1)
