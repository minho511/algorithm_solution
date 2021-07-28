# 2021 07 26 수학 정수론
# https://www.acmicpc.net/problem/1037
n = int(input())
array = sorted(list(map(int, input().split())))
if n % 2 == 1:
    print(array[n//2]**2)
else:
    print(array[0]*array[-1])