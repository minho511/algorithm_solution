class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 1:
            return 1
        k = 0
        for i in range(len(s)):
            ss = ""
            for j in range(i, len(s)):
                if s[j] in ss:
                    break
                else:
                    ss+=s[j]
                
                ans = max(ans, len(ss))
        return ans