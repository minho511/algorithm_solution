import sys; input = sys.stdin.readline
from collections import defaultdict, deque

for t in range(int(input())):
    print(f"Case #{t+1}:")
    n = int(input())
    nums = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(1, n+1):
        graph[nums[i-1]].append(i)
    
    for i in range(1, n+1):
        visit = [0]*(n+1)
        q = deque([i])
        while q:
            nw = q.popleft()
            visit[nw]=1
            for nx in graph[nw]:
                if visit[nx] == 1: continue
                q.append(nx)
        print(sum(visit))

    