# 2022 1 2 스택
# https://leetcode.com/problems/valid-parentheses/
# Runtime: 16 ms
# Memory Usage: 13.5 MB
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False

                k = stack.pop()
                if c == ")" and k != "(":
                    return False
                elif c == "}" and k != "{":
                    return False
                elif c == "]" and k != "[":
                    return False
        return not stack

# 딕셔너리를 만들어 매칭시키는 방법도 있음