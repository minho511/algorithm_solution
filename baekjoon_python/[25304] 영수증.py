# type of problem
# link
import sys; input=sys.stdin.readline

x = int(input())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    x-=a*b
print("Yes" if x == 0 else "No")