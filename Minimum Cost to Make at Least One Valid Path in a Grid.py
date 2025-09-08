from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        dq = deque([(0, 0, 0)])
        
        while dq:
            cost, x, y = dq.popleft()
            
            if cost > dist[x][y]:
                continue
                
            if x == m - 1 and y == n - 1:
                return cost
            
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + (0 if grid[x][y] == i + 1 else 1)
                    
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        
                        if grid[x][y] == i + 1:
                            dq.appendleft((new_cost, nx, ny))
                        else:
                            dq.append((new_cost, nx, ny))
        
        return dist[m - 1][n - 1] 