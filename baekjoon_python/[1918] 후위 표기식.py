# 2021 08 14
# https://www.acmicpc.net/problem/1918
s = list(map(str, input()))
stack = []
result = ""
for i in s:
    print(stack)
    if i.isalpha():
        result+=i
    elif i == '(':
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            result += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
while stack:
    result += stack.pop()
print(result)