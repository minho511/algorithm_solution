# 정렬
# https://www.acmicpc.net/problem/10867
import sys; input=sys.stdin.readline
input()
nums = list(set(map(int, input().split())))
nums.sort()
print(*nums)