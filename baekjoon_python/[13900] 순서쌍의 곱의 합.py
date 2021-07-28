# 2021 07 04 수학
input()
array = list(map(int, input().split()))
answer = 0
r = sum(array)
for i in array:
    r -= i
    answer += i * r
print(answer)