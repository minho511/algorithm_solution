# 2021 07 22 자료 구조 우선순위 큐 트리를 사용한 집합과 맵
# https://www.acmicpc.net/problem/7662
import heapq
import sys; input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    p = []
    q = []
    v = [1]*1000001
    i = 0
    for _ in range(k):
        s, n = input().split()
        if s == "I":
            heapq.heappush(q, (int(n),i))
            heapq.heappush(p, (-(int(n)),i))
            i+=1
        elif s == "D":
            if int(n) == 1:  # 최대힙
                while p and v[p[0][1]] == 0:
                    heapq.heappop(p)
                if p:
                    tm = heapq.heappop(p)
                    v[tm[1]] = 0
            else:           # 최소힙
                while q and v[q[0][1]] == 0:
                    heapq.heappop(q)
                if q:
                    tm = heapq.heappop(q)
                    v[tm[1]] = 0
    while p and v[p[0][1]] == 0:
        heapq.heappop(p)
    while q and v[q[0][1]] == 0:
        heapq.heappop(q)
    if p and q:
        print(-(p[0][0]), q[0][0])
    else:
        print("EMPTY")