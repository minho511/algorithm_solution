# 2021 07 16 문자열 해싱
# https://www.acmicpc.net/problem/15829
import sys; input=sys.stdin.readline
n = int(input())
s = input()
hashing = 0
for i in range(n):
    hashing =(hashing + (31**i * (ord(s[i])-96)))%1234567891
print(hashing)