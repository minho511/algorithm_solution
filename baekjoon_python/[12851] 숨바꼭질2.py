# 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/12851
import sys; input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

if k <n:
    print(n-k)
    print(1)
    exit()
elif k == n:
    print(0) 
    print(1)
    exit()

track = [0]*(100001)

ans1,  ans2 = 0, 0

q = deque([n])
while q:
    x = q.popleft()
    check = track[x]
    if x == k:
        ans1 = check
        ans2+=1
        continue
    move = [2*x, x-1, x+1]
    for m in move:
        if m<0 or m>100000:
            continue
        if track[m]==0 or track[m] == track[x]+1:
            q.append(m)
            track[m] = check+1

print(ans1)
print(ans2)
