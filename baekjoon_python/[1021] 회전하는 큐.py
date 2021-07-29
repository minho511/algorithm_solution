# 2021 07 30 덱 자료구조
# https://www.acmicpc.net/problem/1021
import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
q = deque(range(1,n+1))
array = list(map(int, input().split()))
cnt = 0
for i in array:
    if q[0] == i:
        q.popleft()
        continue
    else:
        std = len(q)//2
        index = q.index(i)
        if index <= std:
            q.rotate(-index)
            cnt += index
        else:
            q.rotate(len(q)-index)
            cnt += len(q)-index
        q.popleft()
print(cnt)