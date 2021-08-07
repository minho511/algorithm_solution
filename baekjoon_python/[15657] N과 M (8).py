# 2021 08 07 백트래킹
# https://www.acmicpc.net/problem/15657
import sys; input = sys.stdin.readline
from itertools import combinations_with_replacement
n, m = map(int, input().split())
array = map(int, input().split())
p = combinations_with_replacement(array,m)
res = []
for i in p:
    res.append(sorted(list(i)))
res.sort()
for i in res:
    print(*i)