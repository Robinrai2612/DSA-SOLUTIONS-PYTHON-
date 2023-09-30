class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        min_i = [nums[0]]

        # Calculate the minimum value for each index 'i' in the array
        for i in range(1, n):
            min_i.append(min(min_i[-1], nums[i]))

        # Iterate through the array from right to left
        for j in range(n - 1, -1, -1):
            # If the current number is equal to the minimum value for its position, skip it
            if nums[j] == min_i[j]:
                continue

            # Check if we found a valid 132 pattern
            while stack and stack[-1] <= min_i[j]:
                stack.pop()

            if stack and stack[-1] < nums[j]:
                return True

            # If not, add the current number to the stack
            stack.append(nums[j])

        return False
