# SELECTION SORT 

'''
SELECTION SORT - TC = O(n^2)  SC = O(1)
BEST CASE(array already sorted) - Time Complexity : O(n^2) , anyhow I need to make comparisons
WORST CASE(unsorted array) - Time Complexity : O(N^2)
USE CASE : generally used for small size arrays, and memory constraints are provided
Selection Sort is an unstable sorting algo
'''

def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    index = -1
    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if arr[j]<arr[index]:
                index = j
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp

arr = [64,25,11,22,18,9]
selectionSort(arr,len(arr))
print(arr)