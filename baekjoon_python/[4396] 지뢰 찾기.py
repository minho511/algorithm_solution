# 2021 07 28 구현 문자열 파싱
# https://www.acmicpc.net/problem/4396
n = int(input())
ground = []
ground2 = []
res = [[0]*n for _ in range(n)]
di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
for _ in range(n):
    ground.append(list(map(str, input())))
for _ in range(n):
    ground2.append(list(map(str, input())))
check = False
for i in range(n):
    for j in range(n):
        if ground2[i][j] == 'x':
            if ground[i][j] == '*':
                check = True
            else:
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni <0 or nj<0 or ni>=n or nj>=n:
                        continue
                    if ground[ni][nj] == '*':
                        res[i][j]+=1
                ground2[i][j] = str(res[i][j])
if check:
    for i in range(n):
        for j in range(n):
            if ground[i][j] == '*':
                ground2[i][j] = '*'
for i in range(n):
    print(''.join(ground2[i]))
