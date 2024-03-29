
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        char_dict = dict({'2':['a','b','c'], 
                            '3':['d', 'e', 'f'],
                            '4':['g','h','i'],
                            '5':['j','k','l'],
                            '6':['m','n','o'],
                            '7':['p','q','r','s'],
                            '8':['t','u','v'],
                            '9':['w','x','y','z']})
        graph = []
        for i in range(len(digits)):
            graph.append(char_dict[digits[i]])
        ans = []
        def dfs(x, y, ss):
            if len(ss) == len(digits):
                ans.append(ss)
                return
            for i in range(len(graph[x])):
                dfs(x+1, i, ss+graph[x][i])
        dfs(0, 0, "")
        return ans