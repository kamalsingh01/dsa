def partition(arr, start, end):
    pivot = arr[end]
    i = start-1
    j = start
    while(j<end):
        if arr[j]<pivot:
            i+=1
            #swap
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j+=1
    i+=1
    temp = arr[i]
    arr[i] = pivot
    arr[end] = temp
    return i #pivot index


def quick_sort(arr, start, end):
    if start<end:
        pivot = partition(arr, start, end)     #partition pivot element ko set krke naya pivot return kr dega
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

if __name__ == "__main__":    
    arr = [6,3,9,5,2,8]
    quick_sort(arr,0, len(arr)-1)
    print(arr)