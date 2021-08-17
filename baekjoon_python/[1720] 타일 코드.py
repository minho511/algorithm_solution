# 2021 08 18 수학 다이나믹프로그래밍 정수론
# https://www.acmicpc.net/problem/1720
n = int(input())
d = [0,1,3]
for i in range(3,n+1):
    d.append(d[i-2]*2 + d[i-1])
if n == 1:
    print(1)
elif n == 2:
    print(3)
elif n%2 == 0:
    print((d[n]-d[n//2])//2+d[n//2]+d[n//2-1])
else:
    print((d[n]-d[n//2])//2+d[n//2])