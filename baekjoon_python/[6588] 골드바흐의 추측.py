# 수학 정수론 소수 판정 에라토스테네스의 체
# https://www.acmicpc.net/problem/6588
import sys; input=sys.stdin.readline

sieve = [True] * 1000001
m = int(1001)
for i in range(3, m + 1, 2):
    sieve[i-1] = False
    if sieve[i] == True:          
        for j in range(i+i, 1000001, i):
            sieve[j] = False
while True:
    n = int(input())
    if n == 0: break
    for i in range(3, n-2):
        if sieve[i] and sieve[n-i]:
            print(f'{n} = {i} + {n-i}')
            break