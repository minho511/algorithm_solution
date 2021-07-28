# 2021 07 12 구현
# https://www.acmicpc.net/problem/9657
array = list(map(int, input().split()))
if array[0] == 1:
    if array == sorted(array):
        print("ascending")
    else:
        print("mixed")
elif array[0] == 8:
    if array == sorted(array, reverse=True):
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")