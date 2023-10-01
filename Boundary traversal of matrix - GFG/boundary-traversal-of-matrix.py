#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        result = []

        # Handle the special case when the matrix has only one row
        if n == 1:
            result.extend(matrix[0])
            return result
    
        # Handle the special case when the matrix has only one column
        if m == 1:
            for i in range(n):
                result.append(matrix[i][0])
            return result
    
        for i in range(m):
            result.append(matrix[0][i])  # Traverse the first row
    
        for i in range(1, n):
            result.append(matrix[i][m - 1])  # Traverse the last column (excluding first and last elements)
    
        for i in range(m - 2, -1, -1):
            result.append(matrix[n - 1][i])  # Traverse the last row (excluding first and last elements)
    
        for i in range(n - 2, 0, -1):
            result.append(matrix[i][0])  # Traverse the first column (excluding first and last elements)
    
        return result
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends