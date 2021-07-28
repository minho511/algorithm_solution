T = int(input())
d = [0] * 1000001
d[1] = 1
d[2] = 2
d[3] = 4
for j in range(4, 1000001):
    d[j] = d[j - 1] + d[j - 2] + d[j - 3]
    d[j] %= 1000000009
for i in range(T):
    k = int(input())
    print(d[k] % 1000000009)
