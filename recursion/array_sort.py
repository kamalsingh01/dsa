def array_sort(arr):
    if len(arr)==1:
        return
    temp = arr.pop()
    array_sort(arr)
    insert(arr, temp)
    
def insert(arr, element):
    if len(arr)==0 or element >arr[-1]:
        arr.append(element)
        return
    temp = arr.pop()
    insert(arr, element)
    arr.append(temp)

if __name__ == "__main__":
    arr = []
    n = int(input(" Enter number of elements in array: "))
    if n==0:
        print("Empty Array")
        exit()
    print("Enter the elements: ")
    for i in range(n):
        arr.append( int(input()) )
    array_sort(arr)
    print("Sorted Array :", arr)


    # def sort_rec(arr,n):
    # if(n==1):
    #     return
    # c_index = n-1
    # sort_rec(arr,c_index)
    # if arr[c_index-1] > arr[c_index]:
    #     temp = arr[c_index-1]
    #     arr[c_index-1] = arr[c_index]
    #     arr[c_index] = temp
    # return

    # arr = [2,3,7,6,4,5,9]
    # sort_rec(arr, len(arr))
    # print(arr)