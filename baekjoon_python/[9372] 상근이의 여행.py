# 그래프 이론 트리
# https://www.acmicpc.net/problem/9372
import sys; input = sys.stdin.readline
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return 1
    if a<b :
        parent[b] = a
    else:
        parent[a] = b
    return 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    parent = [i for i in range(n+1)]
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        cnt += union(parent, a, b)
    
    print(m-cnt)