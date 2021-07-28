# 2021 07 04 수학 정수론 소수판정 에라토스테네스의 체
import sys, math
input = sys.stdin.readline


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        cnt += is_prime_number(i)
    print(cnt)
