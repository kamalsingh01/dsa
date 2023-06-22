# Find a number in  a  row-wise and column wise sorted Matrix
'''
74. Search a 2D Matrix
Medium
12.7K
355
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]], target = 3
Output: true

We can see rows and columns both are sorted. 
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

URL: https://leetcode.com/problems/search-a-2d-matrix/description/

Reference : https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

Approach: 1. We apply linear search and traverse each element and compare with target element, TC = O(n^2)
Approach 2 : We apply Binary Search starting from elemnt at the right top corner of the martrix and check if it is the target element. 
            return -1 if target element not found
'''

#Approach 2 : TC = O(n), O(M+N) for different dimensions of matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m-1
        print(matrix[i][j])
        while( i<n and j>=0 ):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:     # decrementing column, exclude current column
                j-=1
            elif matrix[i][j] < target:     # lowering rows, exclude current row
                i+=1
        return False