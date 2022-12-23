# 수학 구현 사칙연산
# https://www.acmicpc.net/problem/2587
import sys; input=sys.stdin.readline
nums = []
for i in range(5):
    nums.append(int(input()))

nums.sort()
print(sum(nums)//5)
print(nums[2])