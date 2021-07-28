# 2021 07 12 수학 다이나믹 프로그래밍 정수론
# https://www.acmicpc.net/problem/1699
n = int(input())
dp = [0]*(n+1)
k = int(n**0.5)
array = [i*i for i in range(k+1)]
for i in range(1, n+1):
    cnt = []
    for j in range(1, k+1):
        if i < array[j]:
            break
        cnt.append(dp[i-array[j]])
    dp[i] = min(cnt)+1
print(dp[n])
