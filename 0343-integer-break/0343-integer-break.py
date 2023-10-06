class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        # Initialize a list to store the maximum product for each integer from 0 to n
        max_product = [0] * (n + 1)

        # Base cases
        max_product[2] = 2
        max_product[3] = 3

        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                max_product[i] = max(max_product[i], j * max_product[i - j])

        return max_product[n]

        