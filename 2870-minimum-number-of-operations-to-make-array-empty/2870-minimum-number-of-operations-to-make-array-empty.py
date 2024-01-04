class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums) #count[n]
        result =0
        for n,c in count.items():
            if c == 1:
                return -1
            result += math.ceil( c /3)
            
        return result
        