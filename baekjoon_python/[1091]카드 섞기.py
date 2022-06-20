# 구현 시뮬레이션
# https://www.acmicpc.net/problem/1091
import sys; input=sys.stdin.readline


def sol():
    n = int(input())
    cards = [0, 1, 2]*(n//3)
    initial = cards.copy()
    tem = initial.copy()
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))
    cnt = 0
    while True:
        if tem == P:
            break
        tem = [cards[i] for i in S]
        if tem == initial:
            return -1
        else:
            cards = tem
            cnt += 1
    return cnt

if __name__=='__main__':
    print(sol())


