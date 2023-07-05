# Find if there is any duplicate in an array:

'''
217. Contains Duplicate
Easy
9.8K
1.2K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
2.9M
Submissions
4.8M
Acceptance Rate
61.2%

URL : https://leetcode.com/problems/contains-duplicate/description/
'''
#Approach using sorting, where we can sort the array and check if arr[i]==arr[i+1], then return True
#   TC = O(nlogn), Sc = O(1)

# Approach using dictionary
# TC = O(n), SC = O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] =1
        return False
    

