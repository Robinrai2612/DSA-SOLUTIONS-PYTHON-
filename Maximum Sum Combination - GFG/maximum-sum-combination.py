#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq
# from itertools import combinations
class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()
        
        # Create a max heap to store sum combinations
        max_heap = []
        
        # Initialize the max heap with the maximum sum combination
        max_heap.append((-A[N-1]-B[N-1], N-1, N-1))
        
        # Keep track of visited combinations
        visited = set((N-1, N-1))
        
        result = []
        
        # Generate the maximum K valid distinct sum combinations
        while K > 0:
            # Get the maximum sum combination from the heap
            sum_val, i, j = heapq.heappop(max_heap)
            result.append(-sum_val)  # Add the positive value to the result
            
            # Generate the next possible combinations
            if i > 0 and (i-1, j) not in visited:
                heapq.heappush(max_heap, (-(A[i-1] + B[j]), i-1, j))
                visited.add((i-1, j))
            if j > 0 and (i, j-1) not in visited:
                heapq.heappush(max_heap, (-(A[i] + B[j-1]), i, j-1))
                visited.add((i, j-1))
            
            K -= 1
        
        return result





        
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends