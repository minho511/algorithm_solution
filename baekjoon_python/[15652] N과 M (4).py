# 2021 07 17 백트래킹
# https://www.acmicpc.net/problem/15652
import itertools
n,m = map(int, input().split())
result = list(itertools.combinations_with_replacement(range(1, n+1),m))
for i in result:
    print(*i)