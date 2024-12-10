class Solution (object):
    def islandPerimeter(self,grid):
        perimeter = 0
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid [i][j]==1:
                    cell_perimeter = 4
                    
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid [ni][nj]==1:
                            cell_perimeter -=1
                            
                    perimeter += cell_perimeter
        return perimeter 
