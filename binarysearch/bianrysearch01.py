def search(arr,n,key):
    start = 0
    end = n-1
    mid = (start + end)//2
    while(start <= end):
        if key == arr[mid]:
            return mid
        #right part
        if key > arr[mid]:
            start = mid+1
        #left part
        elif key < arr[mid]:
            end = mid-1
        mid = (start + end)//2
    return -1


if __name__ == "__main__":
    arr1 = [2,4,6,8,12,18]
    arr2 = [3,8,11,14,16]
    key=14
    index = search(arr2, len(arr2),key)
    if index!=-1:
        print("Element found at index: ", index)
    else:
        print("element not found")
