# 구현 자료 구조 문자열 스택
# https://www.acmicpc.net/problem/17413
import sys; input=sys.stdin.readline().rstrip

s = input()

result = ""
word = ""
in_tag = False
for i in range(len(s)):
    if s[i]=='<':
        in_tag = True
        result += word
        word = ""
        result += s[i]
    elif s[i] == '>':
        in_tag= False
        result += s[i]
    else:
        if in_tag:
            result += s[i]
        else:
            if s[i] == ' ':
                result += word + ' '
                word = ""
            else:
                word = s[i]+word
if word:
    result += word
print(result)