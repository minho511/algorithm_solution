n = int(input())
array = list(map(int, input().split()))
min_value = int(1e9)
for i in range(n-1):
    min_value = min(abs(array[i+1]-array[i]),min_value)
    if min_value == 0:
        break
print(min_value)