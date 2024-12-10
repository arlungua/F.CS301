class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
      
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            isPrerequisite[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPrerequisite[i][k] and isPrerequisite[k][j]:
                        isPrerequisite[i][j] = True
        
        result = []
        for u, v in queries:
            result.append(isPrerequisite[u][v])
        
        return result
