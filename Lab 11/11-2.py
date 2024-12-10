class Solution(object):
    def checkValidString(self, s):
    
        def dfs(index, openCount):
            if index == len(s):
                return openCount == 0
            
            if openCount < 0:
                return False
            
            char = s[index]
            
            if char == '(':
                return dfs(index + 1, openCount + 1)
            elif char == ')':
                return dfs(index + 1, openCount - 1)
            elif char == '*':
                return (
                    dfs(index + 1, openCount + 1) or 
                    dfs(index + 1, openCount - 1) or  
                    dfs(index + 1, openCount)         
                )
        
        return dfs(0, 0)
