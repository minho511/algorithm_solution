import sys; input = sys.stdin.readline

n = int(input())

res, res2 = [0, 0, 0],[0, 0, 0]
tmp, tmp2 = [0, 0, 0],[0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().split())
    
    for j in range(3):
        if j == 0:
            tmp[j] = a + max(res[j], res[j + 1])
            tmp2[j] = a + min(res2[j], res2[j + 1])
        elif j == 1:
            tmp[j] = b + max(res[j - 1], res[j], res[j + 1])
            tmp2[j] = b + min(res2[j - 1], res2[j], res2[j + 1])
        else:
            tmp[j] = c + max(res[j], res[j - 1])
            tmp2[j] = c + min(res2[j], res2[j - 1])
    
    for j in range(3):
        res[j] = tmp[j]
        res2[j] = tmp2[j]

print(max(res), min(res2))