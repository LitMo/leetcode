class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return (-1)
        fresh_flag = False
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # create a queue and push rotten cell into it
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_flag = True
        # return 0 if no fresh at all
        if not fresh_flag:
            return (0)
        # return -1 if no rotten
        if not queue:
            return (-1)
        # initialize time
        time = 0
        
        while True:
            new_queue = []
            for i, j in queue:
                for direct in directions:
                    new_i, new_j = i+direct[0],j+direct[1]
                    if 0<=new_i < len(grid) and 0<=new_j <len(grid[0]) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        new_queue.append([new_i, new_j])
            queue = new_queue
            if not queue:
                break
            print(queue)
    
            time +=1
        # return -1 if not be able to reach remaining orange
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (-1)
        return time
