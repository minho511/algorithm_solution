#2021 6 28
n = int(input())
tem = n
table = [['*' for _ in range(n)] for _ in range(n)]

def star(num):
    global tem
    num = int(num/3)
    for k in range(num, tem - num + 1, 3*num):
        for q in range(num, tem - num + 1, 3*num):
            for i in range(k, k + num):
                for j in range(q, q + num):
                    table[i][j] = ' '
    if num == 1:
        return
    return star(num)

star(n)
for i in range(n):
    for j in range(n):
        print(table[i][j], end='')
    print()
