# 2021 07 05 수학
n = int(input())
x = 4032
for i in range(9, n+1):
    x *= i
    while x % 10 == 0:
        x //= 10
    x = x % 1000000000000
print(str(x)[-5:])
