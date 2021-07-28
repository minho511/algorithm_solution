# 2021 07 03 브루트포스 알고리즘
import sys
input= sys.stdin.readline

height = []
for _ in range(9):
    height.append(int(input()))

k = []
for i in range(9):
    for j in range(i+1,9):
        k.append((i, j))
result = []
for q in k:
    cnt = 0
    for i in range(9):
        if i == q[0] or i == q[1]:
            continue
        cnt += height[i]
    if cnt == 100:
        for i in range(9):
            if i == q[0] or i == q[1]:
                continue
            result.append(height[i])
        break
result.sort()
for i in result:
    print(i)
