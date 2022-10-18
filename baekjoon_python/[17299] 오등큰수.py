# 자료 구조 스택
# https://www.acmicpc.net/problem/17299
import sys; input=sys.stdin.readline

from collections import Counter
import sys; input = sys.stdin.readline
n = int(input())
NGF = [-1]*n
nums = list(map(int, input().split()))
F = Counter(nums)

tm = nums.pop()
M = F[tm]
stack = [tm]
while nums:
    k = nums.pop()
    if F[k] >= M:
        stack.append(k)
        M = max(F[k], M)
        continue
    for i in range(len(stack)):
        t = stack[len(stack)-i-1]
        if F[k] < F[t]:
            NGF[len(nums)] = t
            break
    stack.append(k)

print(*NGF)