class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return[all(arr[i+1]-arr[i]==arr[1]-arr[0]for i in range(len(arr)-1))for arr in[sorted(nums[a:b+1])for a,b in zip(l,r)]] 