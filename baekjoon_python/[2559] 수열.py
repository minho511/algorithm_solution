# 누적 합 두 포인터 슬라이딩 윈도우
# https://www.acmicpc.net/problem/2559
import sys; input=sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))
data = [0]
accum = 0
for i in temperature:
    accum += i
    data.append(accum)
coll = []
for i in range(k, n+1):
    coll.append(data[i]-data[i-k])
#print(coll)
print(max(coll))