# 2021 07 17 백트래킹
# https://www.acmicpc.net/problem/15651
import itertools
n,m = map(int, input().split())
result = list(itertools.product(range(1, n+1),repeat=m))
for i in result:
    print(*i)