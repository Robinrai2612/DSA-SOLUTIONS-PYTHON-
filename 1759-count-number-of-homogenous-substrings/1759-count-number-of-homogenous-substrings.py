class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=10**9+7
        prev='X'
        count=0
        ans=0
        for c in s:
            if c!=prev:
                ans=(ans+count*(count+1)//2)% mod
                count=1
            else:
                count+=1
            prev=c
        ans=(ans+count*(count+1)//2)% mod
        return ans