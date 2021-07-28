# 2021 07 24
# https://www.acmicpc.net/problem/11659
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sumlist = [0]
sum = 0
for i in nums:
    sum+=i
    sumlist.append(sum)
for _ in range(m):
    a, b = map(int, input().split())
    print(sumlist[b]-sumlist[a-1])
    sys.stdout.write(str())