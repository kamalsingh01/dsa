# BUBBLE SORT

'''

BUBBLE SORT - TC = O(n^2)  SC = O(1)
BEST CASE(array already sorted) - Time Complexity : O(n) , we can opt out after first round of comparisons, as no swapping is performed
WORST CASE(unsorted array) - Time Complexity : O(N^2)
(n-1) rounds of check is required for n number of elements in array
after every ith round, ith largest number marks on the right side of the array
Bubble Sort is an stable sorting algo and in-place sorting algo
USE CASE : generally used for small size arrays, and memory constraints are provided

'''

def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [74,89,11,2,18,9]
bubbleSort(arr,len(arr))
print(arr)