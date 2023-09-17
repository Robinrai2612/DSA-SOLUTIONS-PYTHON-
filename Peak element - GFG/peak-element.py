
class Solution:   
    def peakElement(self,arr, n):
        left, right = 0, n - 1
    
        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle index
            
            # Check if the middle element is a peak by comparing it with its neighbors
            if arr[mid] > arr[mid + 1]:
                right = mid  # If it's a peak, search the left half
            else:
                left = mid + 1  # Otherwise, search the right half
        
        return left  # 'left' will c
            # Code here



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends