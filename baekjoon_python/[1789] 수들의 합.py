# 2021 07 07 그리디 수학
s = int(input())
k = 1
while k*(k+1) <= s*2:
    k += 1
print(k-1)

# import sys
# cases = sys.stdin.read().splitlines()
# for i, case in enumerate(cases):
#     L, P, V = map(int,case.split())
#     if L == 0 and P == 0 and V == 0:
#         break
#     answer = ((V // P) * L) + min(V%P, L)
#     print("Case {}: {}".format(i+1, answer))