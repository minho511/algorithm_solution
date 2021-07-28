# 2021 07 14
# https://www.acmicpc.net/problem/2609
n, m = map(int, input().split())
if n>m:
    n,m = m,n
check1 = 1
for i in range(1,n+1):
    if n%i == 0 and m%i == 0:
        check1 = i
check2 = 0
for i in range(1,n+1):
    if m*i % n == 0:
        check2 = m*i
        break
print(check1)
print(check2)