# 자료 구조 그래프 이론 그래프 탐색 분리 집합
# https://www.acmicpc.net/problem/1043
import sys; input = sys.stdin.readline
from collections import deque, defaultdict

n, m = map(int, input().split())
know_truth = list(map(int, input().split()))

graph = defaultdict(list)
party = {}
ans =[1]*(m)
for p in range(m):
    inp = list(map(int, input().split()))
    party[p] = inp[1:]
    for person in inp[1:]:
        graph[person].append(p)
visited = [False]*(n+1) # 조사한 사람

if know_truth[0] == 0: # 진실을 아는 사람이 없으면 파티개수가 답
    print(m)
    exit()
    
for c in know_truth[1:]:
    q = deque([c])
    while q:
        x = q.popleft()
        # x가 속한 파티조사
        for p in graph[x]: # p는 파티번호
            # 조사한적이 있어서 거짓말 할 수없다고 판단한 파티일때 continue
            if ans[p] == 0:
                continue
            ans[p] = 0 # 거짓말 할수없는 파티처리
            for k in party[p]: # 그 파티에 속한 사람을 q에 넣음
                if visited[k]:
                    continue
                visited[k] = True # 조사한 사람 처리
                q.append(k)
print(sum(ans))