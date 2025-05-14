# https://leetcode.com/problems/combinations/
# 2024-04-26

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        #return list(itertools.combinations(list(range(1, n+1)), k))
        nums = list(range(1, n+1))
        result = []

        def DFS(arr, candi):
            if len(arr) == k:
                result.append(arr)
                return
            temp = candi[:]
            while temp:
                i = temp.pop(0)
                if i not in arr:
                    DFS(arr+[i], temp)
                
        DFS([], nums)
        return result