# 2021 6 29 구현/브루트포스 알고리즘

n, m = map(int, input().split())
sq = [list(map(int, input())) for _ in range(n)]
d = n

check = False
while d > 0:
    if check is True: break
    for i in range(n-d+1):
        if check is True: break
        for j in range(m-d+1):
            if sq[i][j] == sq[i+d-1][j] == sq[i][j+d-1] == sq[i+d-1][j+d-1] and check is False:
                print(d*d)
                check = True
                break
    d -= 1