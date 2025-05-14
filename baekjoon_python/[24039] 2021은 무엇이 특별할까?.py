import sys; input = sys.stdin.readline

n = int(input())

k = 5000
eche = [1]*k
m = int(k**.5)
for i in range(2, m+1):
    if eche[i]:
        for j in range(i*i, k, i):
            eche[j] = 0
f, s = 0, 0

for i in range(2, k):
    if eche[i]:
        f = s
        s = i
        if s*f > n:
            print(s*f)
            exit()
    