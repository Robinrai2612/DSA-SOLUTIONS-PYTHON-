#User function Template for python3

class Solution:
    def rotate(self, N, D):
        ans = []
        D  = D % 16
        bits = [0] * 16
     
        for i in range(16):
            bits[i] = N % 2
            N //= 2
     
        sum_val = 1
        left = 0
        right = 0
     
        i = (16 - D) % 16
        for j in range(16):
            if bits[i] == 1:
                left += sum_val
            sum_val *= 2
            i = (i + 1) % 16
     
        sum_val = 1
     
        i = D
        for j in range(16):
            if bits[i] == 1:
                right += sum_val
            sum_val *= 2
            i = (i + 1) % 16
     
        ans.append(left)
        ans.append(right)
     
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends