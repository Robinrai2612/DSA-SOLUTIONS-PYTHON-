class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                # Swap odd and even elements
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] % 2 == 0:
                # Move left pointer to the right
                left += 1
            elif nums[right] % 2 == 1:
                # Move right pointer to the left
                right -= 1

        return nums




        