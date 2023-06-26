def insert_ele(arr, ele):
    if len(arr)==0 or ele > arr[-1]:
        arr.append(ele)
        return
    
    ele = arr.pop()
    insert_ele(arr, ele)
    arr.append(ele)

def stack_sort(arr):
    if len(arr)!=0:
        temp = arr.pop()
        stack_sort(arr)
        insert_ele(arr,temp)



if __name__ == "__main__":
    arr = [4,6,3,2,9]
    # n = int(input(" Enter number of elements in array: "))
    # if n==0:
    #     print("Empty Array")
    #     exit()
    # print("Enter the elements: ")
    # for i in range(n):
    #     arr.append( int(input()) )
    print(" Unsorted Stack : ", arr)
    stack_sort(arr)
    print("Sorted Stack :", arr[::-1])