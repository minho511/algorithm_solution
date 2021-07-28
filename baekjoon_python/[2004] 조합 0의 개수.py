# 2021 07 28 수학 정수론
# https://www.acmicpc.net/problem/2004
n, m = map(int, input().split())

def count(num, target):
    cnt = 0
    k = target
    while k<=num:
        cnt+=num//k
        k*=target
    return cnt

def count0(n,m):
    cnt5 = count(n,5)-count(n-m,5)-count(m,5)
    cnt2 = count(n,2)-count(n-m,2)-count(m,2)
    return min(cnt5, cnt2)

print(count0(n,m))