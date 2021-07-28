# 2021 07 04 수학
n, l = map(int, input().split())
while True:
    if l > 100:
        print(-1)
        break
    tf = False
    if l%2 == 1:
        std = n%l
        check = n // l
        q = check+l//2+1
    else:
        std = (n+(l//2)) % l
        check = (n + (l // 2)) // l
        q = check+l//2
    if std == 0:
        for i in range(check-l//2, q):
            if i < 0:
                tf = True
                break
            print(i, end=' ')
        if tf is True:
                l += 1
                continue
        break
    l += 1

