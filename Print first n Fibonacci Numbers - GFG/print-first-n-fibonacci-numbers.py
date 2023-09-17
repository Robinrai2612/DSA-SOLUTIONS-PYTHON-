#User function Template for python3

class Solution:
    def printFibb(self,n):
        ans=[]
        x=int(0)
        y=int(1)
        while n>0:
            x,y=y,x+y
            ans.append(x)
            n-=1
        return ans
        # if n <= 0:
        #     return []
    
        # fib_nums = [1, 1]  # Initialize the list with the first two Fibonacci numbers
    
        # while len(fib_nums) < n:
        #     next_fib = fib_nums[-1] + fib_nums[-2]  # Calculate the next Fibonacci number
        #     fib_nums.append(next_fib)
    
        # return fib_nums


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends