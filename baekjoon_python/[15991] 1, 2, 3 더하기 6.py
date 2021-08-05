# 2021 08 05 다이나믹프로그래밍
# https://www.acmicpc.net/problem/15991
import sys; input = sys.stdin.readline
array = [1,1,2,2,3,3]+[0]*99995
for i in range(6, 100001):
    if i % 2 == 0:
        array[i] = (array[i-2] + array[i-4] + array[i-6])%1000000009
    else:
        array[i] = array[i-1]
for _ in range(int(input())):
    n = int(input())
    sys.stdout.write("{}\n".format(array[n]))
