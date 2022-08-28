# 구현 문자열
# https://www.acmicpc.net/problem/10988
import sys; input=sys.stdin.readline().rstrip
s = input()
print(int(s == s[::-1]))