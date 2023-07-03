# Sort Colors

'''
75. Sort Colors
Medium
15.5K
547
Companies
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

URL : https://leetcode.com/problems/sort-colors/

'''

# Brute Force Approach  : sort the array with Merge Sort or Quick Sort where TC = O(n.logn) and SC = O(n)

# Better Approach :
#  Keeping the count of occurence of each color, like creating three variables, one for each number and once counting is done, filling the array again with 
# counted values for the respective number
# TC = O(N)+O(N) and Sc = O(1)

def better_count(nums):
    count_0, count_1, count_2 = 0,0,0
    i=0
    while(i<len(nums)):
        if nums[i]==0:
            count_0+=1
        if nums[i]==1:
            count_1+=1
        if nums[i]==2:
            count_2+=1
        i+=1
    i=0
    while(i<len(nums)):
        if count_0!=0:
            nums[i]=0
            count_0-=1
        elif count_1!=0:
            nums[i]=1
            count_1-=1
        elif count_2!=0:
            nums[i]=2
            count_2-=1
        i+=1



if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    better_count(nums)
    print(nums)