class Solution(object):
    def openLock(self, deadends, target):
        
        dead_set = set(deadends)
        visited = set()

        def dfs(position, steps):
            if position in dead_set or position in visited:
                return float('inf')  
            if position == target:
                return steps
            
            visited.add(position)
            
            min_steps = float('inf')
            for i in range(4):
                for direction in (-1, 1):
                    next_position = list(position)
                    next_position[i] = str((int(next_position[i]) + direction) % 10)
                    next_position = ''.join(next_position)
                    min_steps = min(min_steps, dfs(next_position, steps + 1))
            
            visited.remove(position)  
            return min_steps

        result = dfs("0000", 0)
        return result if result != float('inf') else -1
