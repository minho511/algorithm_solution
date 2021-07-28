# 2021 07 12 다이나믹 프로그래밍 임의 정밀도 / 큰 수 연산
# https://www.acmicpc.net/problem/10826
n = int(input())
d = [0]*(n+2)
d[0] = 0
d[1] = 1
if n>=2:
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
print(d[n])