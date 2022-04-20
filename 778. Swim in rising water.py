## https://leetcode.com/problems/swim-in-rising-water/

## Topic: BFS 
## 
## Dijstra similar & prior-queue

## Time: O(N**2 * logN), perform pq (logN*N) = 2*logN on upto N**2 Nodes
## Space: O(N**2), up to N**2 nodes for the pq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pq = [(grid[0][0], 0, 0)]
        res = 0 
        visited = {(0,0)}
        while pq:
            height, x, y = heapq.heappop(pq)
            res = max(res, height)
            if x == y == N-1:
                return res
            for new_x, new_y in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
                if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in visited:
                    heapq.heappush(pq, (grid[new_x][new_y], new_x, new_y))
                    visited.add((new_x,new_y))
