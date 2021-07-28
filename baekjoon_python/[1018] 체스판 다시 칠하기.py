# 2021 07 14 브루트포스
# https://www.acmicpc.net/problem/1018
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
s = []
for i in range(n):
     s.append(list(map(str,input()[:-1])))

cnt_array = []
for k in range(n - 7):
    for p in range(m - 7):
        cnt = 0
        for i in range(k, k+8):
            for j in range(p, p+8):
                # 먼저 왼쪽위가 B인 체스판을 만들기 위해 다시 칠해야하는 칸 개수를 센다
                if (i+j)%2 == 0 and s[i][j] != 'B':
                    cnt += 1
                elif (i+j)%2 == 1 and s[i][j] != 'W':
                    cnt += 1
        # 왼쪽위가 W인 체스판을 만드는 경우를 비교하여 작은수를 저장
        cnt_array.append(min(cnt, 64-cnt))
print(min(cnt_array))
