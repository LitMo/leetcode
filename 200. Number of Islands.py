class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return (0)
        res = 0
        self.direction = [(1,0), (-1,0), (0, 1), (0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    res +=1
        return res
                
    def dfs(self, i, j, grid):
        grid[i][j] = 0
        for direct in self.direction:
            new_i, new_j = i+direct[0], j+direct[1]
            if 0<= new_i <len(grid) and 0<= new_j<len(grid[0]) and grid[new_i][new_j] == '1':
                self.dfs(new_i, new_j, grid)
        
                
