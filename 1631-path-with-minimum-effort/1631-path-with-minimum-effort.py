class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
    
        # Define the four possible directions: up, down, left, right.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Function to check if it's possible to reach the target with a given effort.
        def canReachTarget(maxEffort):
            visited = [[False] * cols for _ in range(rows)]
            stack = [(0, 0)]

            while stack:
                x, y = stack.pop()
                visited[x][y] = True

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                        diff = abs(heights[new_x][new_y] - heights[x][y])
                        if diff <= maxEffort:
                            stack.append((new_x, new_y))

            return visited[rows - 1][cols - 1]

        # Perform binary search to find the minimum effort required.
        left, right = 0, int(1e6)

        while left < right:
            mid = (left + right) // 2

            if canReachTarget(mid):
                right = mid
            else:
                left = mid + 1

        return left