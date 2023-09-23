# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Calculate the total sum of all elements in the array
        total_sum = sum(A)
        # Initialize variables to keep track of the left sum and right sum
        left_sum = 0
        right_sum = 0
        
        # Iterate through the array
        for i in range(N):
            # Update the right sum by subtracting the current element from the total sum
            right_sum = total_sum - left_sum - A[i]
            # If the left sum is equal to the right sum, return the current index as the equilibrium point
            if left_sum == right_sum:
                return i + 1  # 1-based indexing
            # Update the left sum by adding the current element
            left_sum += A[i]
        
        # If no equilibrium point is found, return -1
        return -1
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends