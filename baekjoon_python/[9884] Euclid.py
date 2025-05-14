import sys; input = sys.stdin.readline
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
a,b = map(int, input().split())

print(gcd(a, b))