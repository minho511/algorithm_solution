# 수학 그래프 이론 그래프 탐색 정수론 유클리드 호제법
# https://www.acmicpc.net/problem/1033
import sys; input=sys.stdin.readline
from collections import defaultdict, deque

# 최대공약수
def gcd(n1, n2):
    t1, t2 = n1, n2
    while t2 > 0:
        t1, t2 = t2, t1 % t2
    return t1

n = int(input())
m = [0]*(n)

info = []
g = defaultdict(list)
for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    g[a].append([b,p,q])
    g[b].append([a,q,p])

start = 0
queue = deque([start])
while queue:
    a = queue.popleft()
    
    for b, p, q in g[a]:
        if m[a] == 0:
            m[a] = p//gcd(p, q)
            m[b] = q//gcd(p, q)
            queue.append(b)
        if m[b] != 0:
            continue
        else:
            visit = [False]*n
            mini = deque([a])
            visit[b] = True
            while mini:
                x = mini.popleft()
                visit[x] = True
                for xx in g[x]:
                    if visit[xx[0]]:
                        continue
                    m[xx[0]] *= p//gcd(p, q)
                    mini.append(xx[0])
            
            m[b] = m[a]*q//gcd(p, q)
            m[a] *= p//gcd(p, q)
            queue.append(b)
e = m[0]
for i in range(1, n):
    e = gcd(e, m[i])

for i in range(n):
    m[i] //=e
print(*m)