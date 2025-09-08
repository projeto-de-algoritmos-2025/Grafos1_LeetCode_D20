from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            
            for i in range(1, k + 1):
                in_degree[i] = 0
            
            for before, after in conditions:
                graph[before].append(after)
                in_degree[after] += 1
            
            queue = deque()
            for node in range(1, k + 1):
                if in_degree[node] == 0:
                    queue.append(node)
            
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return result if len(result) == k else []
        
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_position = {num: idx for idx, num in enumerate(row_order)}
        col_position = {num: idx for idx, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            row = row_position[num]
            col = col_position[num]
            matrix[row][col] = num
        
        return matrix