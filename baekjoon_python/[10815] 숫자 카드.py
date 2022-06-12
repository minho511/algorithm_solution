# 자료 구조 정렬 이분 탐색
# https://www.acmicpc.net/problem/10815
from bisect import bisect, bisect_left
import sys; input=sys.stdin.readline

def binsearch(data, target):
    idx = bisect_left(data , target)
    if idx < len(data) and data[idx] == target:
        return 1
    else:
        return 0

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
for card in list(map(int, input().split())):
    print(binsearch(cards, card), end=' ')
