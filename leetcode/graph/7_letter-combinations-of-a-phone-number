# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 2024-04-24

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {'2': 'abc', '3' : 'def', '4':'ghi', '5':'jkl', '6':'mno', \
                    '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        result = []
        if digits == "":
            return []
        def DFS(comb: str):
            if len(comb) == len(digits):
                result.append(comb)
                return
            for a in graph[digits[len(comb)]]:
                DFS(comb+a)

        DFS("")
        return result
