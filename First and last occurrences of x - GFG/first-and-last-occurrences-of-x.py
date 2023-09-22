#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        first_occurrence = -1
        last_occurrence = -1
        
        # Binary search for the first occurrence
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                first_occurrence = mid
                high = mid - 1  # Continue searching on the left side for the first occurrence
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        # Binary search for the last occurrence
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                last_occurrence = mid
                low = mid + 1  # Continue searching on the right side for the last occurrence
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return first_occurrence, last_occurrence
        
        # code here


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends