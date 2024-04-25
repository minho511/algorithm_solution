# https://leetcode.com/problems/permutations/
# 2024-04-25

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def DFS(p: List[int]):
            if len(p) == len(nums):
                result.append(p)
                return
            for n in nums:
                if n not in p:
                    DFS(p+[n])

        DFS([])

        return result