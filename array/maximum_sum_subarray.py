# Maximum Sum Subarray: kadane's Algorithm
'''
53. Maximum Subarray
Medium


Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
 
URL: https://leetcode.com/problems/maximum-subarray/description/
'''


def max_sum_sub(nums):
    
    # BruteForce Solution - TC = O(n^3) and SC = O(1)
    #
    # total = -100000
    # maximum = -100000
    # for i in range(len(arr)):
    #     for j in range(i,len(arr)):
    #         total = sum(arr[i:j])
    #         if total>maximum:
    #             maximum = total
    # return maximum

    # Better Solution = TC= O(n^2) and SC = O(1) - TLE: 201/210
    # current = -10000
    # maximum = -10000
    # for i in range(len(nums)):
    #     current = 0
    #     for j in range(i,len(nums)):
    #         current = current + nums[j]
    #         if current>maximum:
    #             maximum = current
    # return maximum

    # Optimal Solution(Kadane's Algorithm) TC = O(n) and SC = O(1) - All test cases passed
    current_sum = 0
    maximum = -10000
    start_index = -1
    end_index = -1
    for i in range(len(nums)):
        if current_sum==0:
            start_index = i
        current_sum  = current_sum + nums[i]
        if current_sum > maximum:
            end_index = i
            maximum = current_sum
        if current_sum < 0:
            current_sum = 0
    print(nums[start_index:end_index+1])  # printing longest sub-array
    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum_sub(nums))