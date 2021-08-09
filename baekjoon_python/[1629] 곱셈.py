# 2021 08 07 수학 분할 정복을 이용한 거듭제곱
# https://www.acmicpc.net/problem/1629
import sys; input = sys.stdin.readline

def mpow(a, b, c):
    if b == 1:
        return a%c
    else:
        tm = mpow(a, b//2, c)
        if b%2 == 0:
            return tm*tm%c
        else:
            return tm*tm*a%c


a, b, c = map(int, input().split())
print(mpow(a,b,c))