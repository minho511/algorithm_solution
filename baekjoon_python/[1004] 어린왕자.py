# 2022 01 15 기하학
# https://www.acmicpc.net/problem/1004

import sys
def sqDistance(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        result = 0
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        for i in range(int(sys.stdin.readline())):
            xa, ya, r = map(int, sys.stdin.readline().split())
            start2point = sqDistance(x1, y1, xa, ya)
            end2point = sqDistance(x2, y2, xa, ya)
            if start2point < r**2 and end2point > r**2:
                result+=1
            elif start2point > r**2 and end2point < r**2:
                result+=1
        print(result)