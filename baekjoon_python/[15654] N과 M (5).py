# 2021 08 07 백트래킹
# https://www.acmicpc.net/problem/15654
import sys; input = sys.stdin.readline
from itertools import permutations
n, m = map(int, input().split())
array = map(int, input().split())
p = list(permutations(array, m))
p.sort()
for i in p:
    print(*i)
