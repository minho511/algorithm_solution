# 2021 07 21 구현 비트마스킹
# https://www.acmicpc.net/problem/11723
import sys; input = sys.stdin.readline
m = int(input())
S = []
for _ in range(m):
    k = list(map(str,input().split()))
    if len(k) == 2:
       n = int(k[1])
    s_in = k[0]
    if s_in == 'add':
        if n not in S:
            S.append(n)
    elif s_in == 'check':
        print(int(n in S))
    elif s_in == 'remove':
        if n in S:
            S.remove(n)
    elif s_in == 'toggle':
        if n in S:
            S.remove(n)
        else:
            S.append(n)
    elif s_in == 'all':
        S = [i for i in range(1,21)]
    elif s_in == 'empty':
        S = []