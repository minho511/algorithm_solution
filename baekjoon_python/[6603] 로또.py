# 수학 조합론 백트래킹 재귀
# https://www.acmicpc.net/problem/6603
import sys; input=sys.stdin.readline
from itertools import combinations
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    for case in combinations(nums[1:],6):
        print(*case)
    print()