# 2021 07 22 자료구조 우선순위큐
# https://www.acmicpc.net/problem/11279
import heapq
import sys
input = sys.stdin.readline
q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x>0:
        heapq.heappush(q, (-x,x))
    if x == 0:
        if q:
            sys.stdout.write(str(heapq.heappop(q)[1]))
            sys.stdout.write('\n')
        else:
            print(0)