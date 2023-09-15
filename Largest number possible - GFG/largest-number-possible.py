#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        if S == 0:
            return 0 if N == 1 else -1
    
        if S > 9 * N:
            return -1
    
        result = [0] * N
    
        for i in range(N):
            if S >= 9:
                result[i] = 9
                S -= 9
            else:
                result[i] = S
                S = 0
    
        # Convert the list of digits to an integer
        largest_number = int(''.join(map(str, result)))
    
        return largest_number
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends