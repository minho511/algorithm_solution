# 2021 07 18 자료구조 스택
# https://www.acmicpc.net/problem/17298
import sys; input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
st = [0]
ans = [-1]*n
i = 1
while st and i<n:
    while st and array[st[-1]] < array[i]:
        ans[st[-1]] = array[i]
        st.pop()
    st.append(i)
    i += 1
print(*ans)