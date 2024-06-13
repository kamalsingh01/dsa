'''
Problem statement : Given an array, we have to find the largest element in the array.

Example : 

Input :  arr = [8,10,35,7,9]
Output : 35 is the largest number in the array.
 

Solutions:

Now there can be multiple solutions to this problem, some can be language specific.

A. initializing a variable 'max' with first number of the array and iterating through the array comparing each value with max. T(n) = O(n)
B. using 'max()' or 'min()' functions. - T(n) = O(n)
C. using sort() method and picking the last element of array - T(n) >= O(nlog(n)) - not relevant
D. Recursive Approach : We recursively iterate through the array and make comparisons on way back and return the number. Argument passed to the function call is an array and the length of array decreases on subsequest calls.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n<= 103
0 <= A[i] <= 103
Array may contain duplicate elements.

'''

arr = [5,1,4,25,9]

# solution A
max_num = arr[0]
for i in arr:
    if i >max_num:
        max_num = i
print("Maximum number: ",max_num)

# solution B
print("Maximum number: ", max(arr))
print("Minimum number: ", min(arr))


# Solution D

def find_max_num(arr):
    if len(arr)==1: return arr[0]
    if arr[0]<find_max_num(arr[1:]): 
        return find_max_num(arr[1:])
    return arr[0]

print("Maximum number using recursion : ",find_max_num(arr))
