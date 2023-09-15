#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(array)
        return expected_sum - actual_sum
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends