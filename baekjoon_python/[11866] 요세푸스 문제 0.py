# 2021 07 13 자료구조 큐
# https://www.acmicpc.net/problem/11866
from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
result =[]
cnt = 0
s = "<"
while q:
    e = q.popleft()
    cnt+=1
    if cnt < k:
        q.append(e)
    else:
        s+="{}, ".format(e)
        cnt=0
print(s[:-2]+">")
