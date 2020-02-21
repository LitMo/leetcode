### BFS Solutions, time O(mn)
import collections
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = collections.deque()
        # Push gate into queue
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        
        # BFS
        while queue:
            x, y = queue.popleft()
            for direct in directions:
                new_x, new_y = x+direct[0], y+direct[1]
                if 0<= new_x < len(rooms) and 0<=new_y < len(rooms[0]) and rooms[x][y]+1 < rooms[new_x][new_y]:
                    rooms[new_x][new_y] = rooms[x][y]+1
                    queue.append([new_x, new_y])
        
        
### DFS solution, easy to code, unstable in terms of performance
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return 
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, rooms)
        
    def dfs(self, i, j, rooms):
        for direct in self.directions:
            new_i, new_j = i + direct[0], j + direct[1]
            if 0<= new_i <len(rooms) and 0<= new_j < len(rooms[0]) and rooms[new_i][new_j] > 0 and rooms[i][j] + 1 < rooms[new_i][new_j]:
                rooms[new_i][new_j] = rooms[i][j] + 1
                self.dfs(new_i, new_j, rooms)
