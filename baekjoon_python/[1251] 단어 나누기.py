# 2021 07 09 구현 문자열 브루트포스 정렬
s = input()
n = len(s)
array = []
for i in range(1, n):
    s1 = s[:i]
    tm_s = s[i:]
    for j in range(1, n-i):
        s2 = tm_s[:j]
        s3 = tm_s[j:]
        array.append(s1[::-1]+s2[::-1]+s3[::-1])
print(min(array))