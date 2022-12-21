# 수학 기하학 피타고라스 정리
# https://www.acmicpc.net/problem/1064
import sys; input=sys.stdin.readline


def solution():
        
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    # exception : Three points are on the same line.
    if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
        return -1.

    # d1 , point 1, 2
    d1 = ((x1-x2)**2 + (y1-y2)**2)**.5
    # d2 , point 1, 3
    d2 = ((x3-x1)**2 + (y3-y1)**2)**.5
    # d3 , point 2, 3
    d3 = ((x3-x2)**2 + (y3-y2)**2)**.5

    # case1
    c1 = 2*(d1 + d2)
    # case2
    c2 = 2*(d1 + d3)
    # case3
    c3 = 2*(d2 + d3)

    # answer
    case = [c1, c2, c3]
    return max(case)-min(case)

if __name__=="__main__":
    ans = solution()
    print(ans)