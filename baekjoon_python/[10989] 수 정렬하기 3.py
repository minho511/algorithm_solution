import sys

n = int(sys.stdin.readline())
count = [0] * 10001
for i in range(n):
    count[int(sys.stdin.readline())] += 1
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)

# 계수정렬 : 데이터의 범위만 한정되어 있다면 효과적으로 사용할 수 있다.
# 항상 빠르게 동작한다
# pypy3 말고 python3로 제출하니까 정답처리
