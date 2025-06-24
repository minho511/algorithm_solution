class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <=57:
                t+=c
        return t == t[::-1]


        