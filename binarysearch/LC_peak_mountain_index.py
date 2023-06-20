# 
'''
852. Peak Index in a Mountain Array
Medium

Companies
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

URL : https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
'''
# Points to note:
'''
    1. ...... < arr[i-2] < arr[i-1] < arr[i] > arr[i+1] > ar[i+2] > ...... where arr[i] is peak index element
    2. on left side arr[mid-1] < arr[mid] < arr[mid+1]
    3. on right side arr[mid-1] > arr[mid] > arr[mid+1]
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)-1
        mid = (start+end)//2
        peak = mid
        temp = mid

        # we will assume that first mid is peak, 
        #then we go to all left to chekc if any number greater than existing peak
        # likewise we go to right and check

        #left part
        end = mid-1
        while(start<=end):
            mid = (start+end)//2
            if arr[mid]>arr[peak]:
                peak = mid
                if arr[mid]<arr[mid+1]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if arr[mid]<arr[mid+1]:
                    start = mid+1
                else:
                    end = mid-1
        
        #right part
        start = temp+1
        end = len(arr)-1
        while(start<=end):
            mid = (start+end)//2
            if arr[mid]>arr[peak]:
                peak = mid
                if arr[mid]<arr[mid-1]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if arr[mid]<arr[mid-1]:
                    end = mid-1
                else:
                    start = mid+1
        
        return peak

    # Optimised Approach
    # s = 0
    # e = len(arr)-1
    # mid = (s+e)//2
    # while(s<e):
    #     if arr[mid]<arr[mid+1]:
    #         s = mid+1
    #     else:
    #         e = mid
    #     mid = (s+e)//2
    # return s