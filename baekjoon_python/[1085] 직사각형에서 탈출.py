import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
print(min(w-x, x, h-y, y))
