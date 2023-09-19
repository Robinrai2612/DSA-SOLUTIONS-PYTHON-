#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        position = 1

        # Iterate through bits of N
        while n > 0:
            # Check if the rightmost bit is set
            if n & 1 == 1:
                return position
    
            # Right shift N to check the next bit
            n >>= 1
            position += 1
    
        # If there are no set bits
        return 0
        
        #Your code here
        

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends