#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
    
        # Helper function to mark land cells as visited
        def mark_visited(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                grid[x][y] = 0  # Mark as visited
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        stack.append((nx, ny))
    
        # Traverse the boundary and mark land cells
        for i in range(rows):
            if grid[i][0] == 1:
                mark_visited(i, 0)
            if grid[i][cols - 1] == 1:
                mark_visited(i, cols - 1)
    
        for j in range(cols):
            if grid[0][j] == 1:
                mark_visited(0, j)
            if grid[rows - 1][j] == 1:
                mark_visited(rows - 1, j)
    
        # Count remaining land cells
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends