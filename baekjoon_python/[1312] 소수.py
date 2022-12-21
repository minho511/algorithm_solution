# 수학
# https://www.acmicpc.net/problem/1312
import sys; input=sys.stdin.readline
a, b, c = map(int, input().split())
tem = a//b
tem = a-tem*b
cnt = 0
while cnt < c:
    tem *= 10
    ans = tem//b
    tem = tem-b*ans
    cnt+=1
print(ans)