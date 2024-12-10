class Solution(object):
    def findOrder(self, numCourses, prerequisites):
       
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        result = []
        is_possible = [True]
        
        def dfs(course):
            if state[course] == 1:
                is_possible[0] = False
                return
            if state[course] == 2:
                return

            state[course] = 1

            for neighbor in graph[course]:
                dfs(neighbor)
                if not is_possible[0]:
                    return

            state[course] = 2
            result.append(course)

        for course in range(numCourses):
            if state[course] == 0:
                dfs(course)
                if not is_possible[0]:
                    return []

        return result[::-1]
