# 2021 07 22 수학
# https://www.acmicpc.net/problem/1676
n = int(input())
if n>=1:
    fact = 1
    for i in range(1, n+1):
        fact*=i
    cnt = 0
    for i in str(fact)[::-1]:
        if i == '0':
            cnt +=1
        else:
            break
    print(cnt)
else:
    print(0)