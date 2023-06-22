# Print Spiral Matrix elements
'''
54. Spiral Matrix
Medium

Companies
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

URL : https://leetcode.com/problems/spiral-matrix/

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)     # number of rows
        n = len(matrix[0])  # number of columns
        lst = []
        left, right, top, bottom = 0, n-1, 0, m-1
        print(left, right, top, bottom)
        while( top<=bottom and left<=right):  # ensures if there are any more columns and rows present to be spiralled
            

            # moving left -> right
            for i in range(left,right+1):
                lst.append( matrix[top][i] )
            top+=1
            
            #moving top->bottom
            for i in range(top, bottom+1):
                lst.append( matrix[i][right] )
            right-=1

            if top<=bottom:         # condition for single rows
                # #moving right->left
                for i in range(right, left-1, -1):
                    lst.append( matrix[bottom][i] )
                bottom-=1

            if left<=right:         # condition for single column
            # #moving bottom->top
                for i in range(bottom, top-1, -1):
                    lst.append( matrix[i][left] )
                left+=1
  
        return lst

    # TC = O(n x m) and SC = O(n x m)