#User function Template for python3
import sys
class Solution:
    def printClosest (self,arr, brr, n, m, x) :
        ans = []
    
        start = 0
        end = m - 1
    
        element1 = float('-inf')
        element2 = float('-inf')
    
        closestDiff = float('inf')
    
        while start < n and end >= 0:
            sum = arr[start] + brr[end]
            absDiff = abs(sum - x)
    
            if absDiff < closestDiff:
                closestDiff = absDiff
                element1 = arr[start]
                element2 = brr[end]
    
            if sum > x:
                end -= 1
            else:
                start += 1
    
        ans.append(element1)
        ans.append(element2)
    
        return ans
            
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends