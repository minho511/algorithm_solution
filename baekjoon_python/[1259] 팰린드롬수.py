# 2021 07 13
# https://www.acmicpc.net/problem/1259
import sys; input = sys.stdin.readline
while True:
    s = input()[:-1]
    if s == '0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')