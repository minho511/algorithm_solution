# 2021 07 11 이분탐색 수학
# https://www.acmicpc.net/problem/2417
n = int(input())
start = 0
end = n
result = 0
while start <= end:
    mid = (start+end)//2
    k = mid**2
    if k == n:
        result = mid
        break
    elif n < k:
        end = mid-1
    elif n > k:
        start = mid+1
        result = mid+1
print(result)