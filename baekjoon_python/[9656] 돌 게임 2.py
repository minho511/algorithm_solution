# 2021 07 12 다이나믹 프로그래밍 게임 이론
# https://www.acmicpc.net/problem/9656

# 다이나믹 프로그래밍
n = int(input())
d = ["SK"]*1001
d[1] = 1
d[2] = 0
d[3] = 1
for i in range(4, 100):
    d[i] = 1-d[i-1]*d[i-3]
if d[n] == 1:
    print("CY")
else:
    print("SK")

# 01010101 반복되는 규칙을 이용한 코드
# k = int(input())%2
# if k == 1:
#     print("CY")
# else:
#     print("SK")