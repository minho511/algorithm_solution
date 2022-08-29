# 프루트포스 알고리즘 백트래킹
# https://www.acmicpc.net/problem/1182
import sys; input=sys.stdin.readline
from itertools import combinations
n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for c in combinations(nums, i):
        if sum(c) == s:
            ans +=1
print(ans)