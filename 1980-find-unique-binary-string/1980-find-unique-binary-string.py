class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        binary_set = set(nums)

        for i in range(2 ** n):
            binary_str = format(i, 'b').zfill(n)
            if binary_str not in binary_set:
                return binary_str
