<<<<<<< HEAD
# 2021 07 22 자료구조 우선순위큐
=======
# 2021 07 22 자료구조 우선순위 큐
>>>>>>> 1a7fe334ed3c60de9ce9c5e9f300671cca90d227
# https://www.acmicpc.net/problem/1927
import heapq
import sys
input = sys.stdin.readline
q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x>0:
        heapq.heappush(q, x)
    if x == 0:
        if q:
            sys.stdout.write(str(heapq.heappop(q)))
            sys.stdout.write('\n')
        else:
            print(0)
