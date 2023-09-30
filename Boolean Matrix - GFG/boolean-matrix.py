#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    
    # Initialize two arrays to track rows and columns to be modified
    row_flag = [0] * R
    col_flag = [0] * C
    
    # Traverse the input matrix and set flags for rows and columns to be modified
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                row_flag[i] = 1
                col_flag[j] = 1
    
    # Modify the matrix based on row and column flags
    for i in range(R):
        for j in range(C):
            if row_flag[i] == 1 or col_flag[j] == 1:
                matrix[i][j] = 1
    # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends