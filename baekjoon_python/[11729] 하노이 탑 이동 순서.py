#2021 07 04 재귀
n = int(input())
print(2**n-1)

def hanoi(k, a, b, c):
    if k == 1:
        print(a, c)
        return
    hanoi(k-1, a, c, b)
    print(a, c)
    hanoi(k-1, b, a, c)

hanoi(n, 1, 2, 3)
