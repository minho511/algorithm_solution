#백준 1904

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1000001
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746
print(d[n])

# 다이나믹프로그래밍을 할때 dp 테이블 크기를 주어진 조건 만큼 잡아주자
