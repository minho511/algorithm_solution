# 2021 08 05 다이나믹프로그래밍
# https://www.acmicpc.net/problem/15989
import sys; input = sys.stdin.readline
array = [0,1,2,3]+[0]*99997
for i in range(4, 10001):
    array[i] = (int(i%3 == 0)+array[i - 1] + array[i - 2] - array[i - 3]) % 1000000009
for _ in range(int(input())):
    n = int(input())
    sys.stdout.write("{}\n".format(array[n]))