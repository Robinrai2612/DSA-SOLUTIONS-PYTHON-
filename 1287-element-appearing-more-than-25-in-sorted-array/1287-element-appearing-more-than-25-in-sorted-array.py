class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4 + 1
        for i in range(len(arr)):
            if arr[i] == arr[i + threshold - 1]:
                return arr[i]