# 수학 구현 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1977
import sys; input=sys.stdin.readline

m = int(input())
s1 = int(m**0.5)
if m**0.5 != s1:
    s1 += 1

n = int(input())
s2 = int(n**0.5)

if s1 > s2:
    print(-1)
elif s1 == s2:
    print(s1**2)
else:
    sum_ = 0
    for i in range(s1, s2+1):
        sum_+=i**2
    print(sum_)
    print(s1**2)
    
