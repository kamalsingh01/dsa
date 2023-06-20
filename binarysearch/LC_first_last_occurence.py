# First and Last Position of an Element In Sorted Array
'''

URL : https://www.codingninjas.com/codestudio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549?source=youtube&campaign=love_babbar_codestudio2
'''
from os import *
from sys import *
from collections import *
from math import *

def firstAndLastPosition(arr, n, k):

    # Write your code here
    min_index, max_index = -1,-1
    count = 0
    start = 0
    end = n-1
    mid = (start+end)//2 
    
    # we find left occurence then we find right occurence seperately using two loops
    # TC = O(logn)

    while(start<=end):
        if arr[mid]==k:
            count+=1
            min_index = mid
            end = mid-1
        if arr[mid] < k:
            start = mid+1
        elif arr[mid] > k:
            end = mid-1
        mid = (start+end)//2

    start = 0
    end = n-1
    mid = (start+end)//2

    while(start<=end):
        if arr[mid]==k:
            count+=1
            max_index = mid
            start = mid+1
        if arr[mid] < k:
            start = mid+1
        elif arr[mid] > k:
            end = mid-1
        mid = (start+end)//2

    print("No. of occurences: ", count)
	
    return min_index, max_index