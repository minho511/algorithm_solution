# 2021 08 17 그리디 level1
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    n_lost = [i for i in lost if i not in reserve]
    n_reserve = [i for i in reserve if i not in lost]
    for a in n_reserve[:]:
        if a-1 in n_lost:
            n_lost.remove(a-1)
            n_reserve.remove(a)
            continue
        if a+1 in n_lost:
            n_lost.remove(a+1)
            n_reserve.remove(a)
            continue
    return n-len(n_lost)