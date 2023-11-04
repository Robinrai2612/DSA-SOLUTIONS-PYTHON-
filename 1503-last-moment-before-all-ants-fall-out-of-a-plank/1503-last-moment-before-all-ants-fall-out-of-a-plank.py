class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_time_left = max(left) if left else 0
        max_time_right = n - min(right) if right else 0

        return max(max_time_left, max_time_right)