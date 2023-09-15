#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        candidate = A[0]
        count = 1
        
        # Iterate through the array
        for i in range(1, N):
            # If the current element is the same as the candidate, increment the count
            if A[i] == candidate:
                count += 1
            # Otherwise, decrement the count
            else:
                count -= 1
            
            # If the count becomes zero, update the candidate to the current element
            if count == 0:
                candidate = A[i]
                count = 1
        
        # Now, candidate may be the majority element, but we need to verify
        count = 0
        for num in A:
            if num == candidate:
                count += 1
        
        # If the count of the candidate is greater than N/2, it's the majority element
        if count > N // 2:
            return candidate
        
        # If there is no majority element, return -1
        return -1
            #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends