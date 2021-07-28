# 수학 구
a, b = map(int, input().split())
array = []
for i in range(1,46):
    for j in range(i):
        array.append(i)
print(array)
print(sum(array[a-1:b]))

# number_list = []
# for i in range(1, 46):
#     number_list += [i] * i
#
# A, B = map(int, input().split())
# print(sum(number_list[A - 1:B]))