# 2021 08 17 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9251
s1 = input()
s2 = input()
l1, l2 = len(s1), len(s2)
graph = [[0]*(l2+1) for _ in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            graph[i][j] = graph[i-1][j-1]+1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])
print(graph[-1][-1])