# 2021 07 14 수학 구현 조합론
# https://www.acmicpc.net/problem/11050
n, k = map(int, input().split())
k = min(k, n-k)
result = 1
for i in range(k):
    result *= n-i
    result //= (i+1)
print(result)

