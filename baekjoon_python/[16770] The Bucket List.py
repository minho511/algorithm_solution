# 2021 07 07 구현 그리디 정렬 시뮬레이션
n = int(input())
array = [0] * 1001
for i in range(n):
    s, t, b = map(int, input().split())
    for j in range(s, t+1):
        array[j] += b
print(max(array))
