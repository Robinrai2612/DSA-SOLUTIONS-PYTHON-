class Solution:
    def duplicates(self, arr, n): 
        frequency = {}
        duplicates = []
        
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for num, freq in frequency.items():
            if freq > 1:
                duplicates.append(num)
        
        if not duplicates:
            return [-1]
        
        return sorted(duplicates)


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends