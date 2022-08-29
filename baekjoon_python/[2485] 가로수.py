# 수학 정수론 유클리드 호제법
# https://www.acmicpc.net/problem/2485
import sys; input=sys.stdin.readline
n = int(input())
nums = []
sub = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
for i in range(1,n):
    sub.append(nums[i]-nums[i-1])
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a
s = gcd(sub[0], sub[-1])
ans = 0
for i in range(len(sub)):
    ans += sub[i]//s-1

print(ans)