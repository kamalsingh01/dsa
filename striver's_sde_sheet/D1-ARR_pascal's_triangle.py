# Program to generate Pascal’s Triangle
'''
118. Pascal's Triangle
Easy
10.3K
332
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

'''

# My solution: Tc = )(n^2) and SC = O(m*n)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        n = numRows
        i=0
        while(i<n):
            temp = []
            if i==0:
                temp.append(1)
                lst.append(temp)
                i+=1
                continue
            for j in range(i+1):
                if j==0:
                    temp.append(1)
                elif j==i:
                    temp.append(1)
                else:
                    temp.append( lst[i-1][j-1] + lst[i-1][j] )          
            lst.append(temp)
            i+=1
        return lst
