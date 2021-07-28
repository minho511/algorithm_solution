# 2021 07 21 수학 구현 문자열 정수론 소수 판정 에라토스테네스의 체
# https://www.acmicpc.net/problem/1990
import sys
a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
def is_prime_number(n):
    m = int(n**0.5)
    for i in range(3,m+1,2):
        if n%i == 0:
            return 0
    return 1

def is_palindrome(n):
    s_n = str(n)
    l = len(s_n)
    for k in range(l//2):
        if s_n[k] != s_n[-k-1]:
            return 0
    return 1

for i in range(a, b+1):
    # 짝수일때 검사하지 않음 / a >=5 이므로 2일때도 고려하지 않는다.
    # 팰린드롬수가 짝수보다 적으므로 먼저 검사
    if not is_palindrome(i):
        continue
    if i % 2 == 0:
        continue
    if is_prime_number(i):
        sys.stdout.write(str(i))
        sys.stdout.write("\n")
print(-1)