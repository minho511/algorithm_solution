import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**(1/2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == abs(r2-r1) or d == r1+r2:
            print(1)
        elif abs(r2 - r1) < d < r1 + r2:
            print(2)
        else:
            print(0)