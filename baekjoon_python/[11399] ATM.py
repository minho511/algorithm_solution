# 2021 07 23 그리디 정렬
# https://www.acmicpc.net/problem/11399
import sys; input =sys.stdin.readline
n = int(input())
p = sorted(list(map(int, input().split())))
sum = 0
res = 0
for i in p:
    sum+=i
    res+=sum
print(res)