class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # Define a modulo constant to prevent integer overflow
        modulo = 1000000007

        # Calculate the maximum possible position on the staircase that can be reached
        max_len = min(arrLen, 1 + steps // 2)

        # Initialize an array to store the number of ways to reach each position on the staircase
        ways = [0] * (max_len + 1)

        # Set the base case: There is one way to stay at the initial position
        ways[0] = 1

        # Iterate through the number of steps taken
        for i in range(steps):
            left = 0

            # Iterate through possible positions on the staircase, considering bounds
            for j in range(min(max_len, i + 2, steps - i + 3)):
                # Calculate the number of ways to reach the current position `j`
                # using the dynamic programming recurrence relation and considering the `left` value
                left, ways[j] = ways[j], (ways[j] + left + ways[j + 1]) % modulo

        # The `ways[0]` value represents the number of ways to reach the top of the staircase
        return ways[0]