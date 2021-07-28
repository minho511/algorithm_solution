# 2021 07 14 자료구조 큐
# https://www.acmicpc.net/problem/2164
from collections import deque
n = int(input())
q = deque([i for i in range(1, n+1)])
check = 1
while q:
    k = q.popleft()
    if check == 1:
        check = 0
        continue
    else:
        check = 1
        q.append(k)
print(k)