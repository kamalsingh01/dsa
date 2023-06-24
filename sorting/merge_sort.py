def conquer(arr, start, mid, end):
    merged = [0]*(end-start+1)
    index1 = start
    index2 = mid+1
    x=0

    while( index1<=mid and index2<=end ):
        if arr[index1]<=arr[index2]:
            merged[x] = arr[index1]
            index1+=1
            x+=1
        else:
            merged[x] = arr[index2]
            index2+=1
            x+=1
    while( index1 <=mid):
        merged[x] = arr[index1]
        index1+=1
        x+=1
    while( index2<=end):
        merged[x] = arr[index2]
        index2+=1
        x+=1
    i=0
    j=start
    while( i<len(merged)):
        arr[j] = merged[i]
        i+=1
        j+=1


def divide(arr,start,end):
    if start>=end:
        return
    mid = (start+end)//2
    divide( arr, start, mid)
    divide( arr, mid+1, end)
    conquer(arr, start, mid, end)
    
    


if __name__ == "__main__":
    arr = [6,3,9,5,2,8]
    divide( arr, 0, len(arr)-1)
    print(arr)