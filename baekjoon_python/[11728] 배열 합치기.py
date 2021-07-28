# 2021 07 28 정렬 두 포인터
# https://www.acmicpc.net/problem/11728
input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(a+b))
