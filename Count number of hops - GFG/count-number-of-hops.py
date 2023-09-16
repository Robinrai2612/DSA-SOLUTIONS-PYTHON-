#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        MOD = 1000000007
        if n <= 2:
            return n
        if n == 3:
            return 4
        
        # Initialize an array to store the number of ways to reach each step.
        ways = [0] * (n + 1)
        
        # There is one way to reach step 0.
        ways[0] = 1
        
        # There is one way to reach step 1, and two ways to reach step 2.
        ways[1] = 1
        ways[2] = 2
        
        # Calculate the number of ways to reach each step from 3 to N.
        for i in range(3, n + 1):
            ways[i] = (ways[i - 1] + ways[i - 2] + ways[i - 3]) % MOD
        
        return ways[n]
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends