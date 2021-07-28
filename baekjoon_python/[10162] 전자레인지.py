# 2021 07 03 수학 구현 그리디
t = int(input())
if t % 10 != 0:
    print(-1)
else:
    print("{} {} {}".format(t//300, t % 300//60, t % 60//10))
