import sys; input = sys.stdin.readline
from itertools import combinations

_, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for d in sorted((set(combinations(nums, m)))):
    print(*d)
