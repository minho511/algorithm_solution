# 2021 07 06 그리디 문자열 구현
import sys
input = sys.stdin.readline

n = int(input())
seats = input()
seats = seats.replace("S", "-1+1-1").replace("LL","-1+2-1").replace("-1-1","-1")
print(min(n, n-eval(seats)))