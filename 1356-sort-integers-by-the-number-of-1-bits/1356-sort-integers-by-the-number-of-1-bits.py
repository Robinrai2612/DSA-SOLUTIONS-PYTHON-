class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(num):
            count = 0
            while num:
                num &= (num - 1)
                count += 1
            return count

        return sorted(arr, key=lambda x: (countBits(x), x))
        