# Finding Square root of a number:
'''
69. Sqrt(x)
Easy

Companies
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

URL : https://leetcode.com/problems/sqrtx/description/

Reference : https://www.geeksforgeeks.org/square-root-of-an-integer/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # Brute Force Approach - TC = O(sqrt(x)) , SC = O(1)
        if x==0 or x==1:
            return x
        i = 1
        result = 1
        while( result <= x): 
            i+=1
            result = i * i
        return i-1

        # Better Approach using Binary Search - TC = O(log(x)), SC = O(1)
        if x == 0 or x==1:
            return x
        s=0
        e = x//2 #because floor of half of the number is always greater than square root of the number
    
        while( s <= e):
            mid = (s+e)//2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                s = mid+1
                ans = mid
            else:
                e = mid-1
        return ans