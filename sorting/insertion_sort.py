# INSERTION SORT
'''
TC = O(n^2), SC = O(1)
'''
def insertionSort(arr, n):
    for i in range(n):
        temp = arr[i]
        j = i-1
        while(j>=0):
            if temp < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j-=1
        arr[j+1] = temp




arr = [4,12,11,59,20,2]
insertionSort(arr, len(arr))
print(arr)