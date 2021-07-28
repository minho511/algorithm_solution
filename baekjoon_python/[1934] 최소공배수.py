# 2021 07 26 수학 정수론 유클리드 호제법
# https://www.acmicpc.net/problem/1934
import sys; input = sys.stdin.readline
def uh(a,b):
    if a<b:
        a,b = b,a
    if b == 0:
        return
    if a%b == 0:
        return b
    else:
        return uh(b, a%b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a*b//uh(a,b))