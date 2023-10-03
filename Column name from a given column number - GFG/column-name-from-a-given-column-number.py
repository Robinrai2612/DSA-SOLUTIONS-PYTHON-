#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        result = ''
    
        while n > 0:
            # Decrement N by 1 to handle 0-based indexing.
            n -= 1
            # Calculate the remainder when N is divided by 26.
            remainder = n % 26
            # Append the corresponding character to the result.
            result = chr(ord('A') + remainder) + result
            # Update N to the quotient when divided by 26.
            n //= 26
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends