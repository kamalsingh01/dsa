'''
73. Set Matrix Zeroes
Medium

Companies
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

# My Solution  - TC = O(m*n)*(n+m) SC = O(n)+O(m*n) - very loose
# I am using the concept of creating transposes and adding them and resultant matrix is the result
class Solution: 
       
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = []
        m = len(matrix)
        n = len( matrix[0] )
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                   visited.append( (i,j))
        for k in visited:
            matrix[k[0]] = [0]*n
        temp = [[0 for x in range(m)] for y in range(n)]
        print(temp)
        for i in range(n):
            for j in range(m):
                temp[i][j] = matrix[j][i]
        for k in visited:
            temp[k[1]] = [0]*m
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[j][i]
        print(matrix)

# Brute Force Solution
 
# First we traverse through the matrix using two loops, and where ever we find 0, we mark all row elemnts and column matrix as -1 excpt other zeroes present in those rows and columns
# after marking all 0s, we again iterate and make all -1 as 0, which will be the final result.
# this solution only works for matrix with no negetive valuesm, we can take any character in place of -1, it will work
# TC = O((m*n)*(m+n)) + O(m*n) SC = O(1) 
# hence its a cubic order function, so we cannot take it as a solution.

class Solution: 
       
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len( matrix[0] )
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    #row marking
                    for k in range(n):
                       if matrix[i][k] != 0:
                           matrix[i][k]=-1  #'a'
                    #column marking
                    for l in range(m):
                        if matrix[l][j] != 0:
                           matrix[l][j]=-1  #'a'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==-1:   #'a'
                    matrix[i][j] = 0
        print(matrix)

# Better Solution

# We take two arrays, row array of size m and column array of size n and initialize them with 0
# whenever there is a zero, we mark 0 to 1 for corresponding rows and columns in the respective arays.
# after complete marking, we again iterate and wherever wither the row and column is marked we make that element of matrix as 0
# TC = O(m*n)+O(m+n) and SC = O(m)+O(n)
# So this gets a auxiliary space, not an optimal solution.

def setZeroes(self, matrix: List[List[int]]) -> None:
        #better solution, but uses SC = O(m)+O(n), extra auxiliary space
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len( matrix[0] )
        row = [0]*m
        column = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
        for i in range(m):
            for j in range(n):
                if row[i] or column[j]:
                    matrix[i][j] = 0
        print(matrix)


# Optimal Solution
# TC = O(m*n) and Sc = O(1)

def setZeroes(self, matrix: List[List[int]]) -> None:
            #Optimal Solution, Tc = O(m*n) uses SC = O(1), no extra auxiliary space
            """
            Do not return anything, modify matrix in-place instead.
            """
            m = len(matrix)
            n = len( matrix[0] )

            col0 = 1
            #col[0] is row[m]
            #row[0] is col[n]
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]==0:
                        matrix[i][0] = 0
                        if j!=0:
                            matrix[0][j] = 0
                        else:
                            col0=0
                        
            for i in range(1,m):
                for j in range(1,n):
                    if matrix[i][j] != 0:
                        #check col and row
                        if matrix[0][j] ==0 or matrix[i][0]==0:
                            matrix[i][j] = 0
                        
            if matrix[0][0] == 0:
                for j in range(n):
                    matrix[0][j] = 0
            if col0 ==0:
                for i in range(m):
                    matrix[i][0] = 0

            print(matrix)
