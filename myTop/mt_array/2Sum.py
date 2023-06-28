

# Naive Approach - TC = O(N) and SC = O(1)
def read(n: int, book: list(), target: int) -> str:
    # Write your code here.
    for i in range(n):
        for j in range(i+1,n):
            if book[i]+book[j] == target:
                return 'YES'
    return 'NO'

# Better Approach( Using Hashing) - TC = O(N) and SC = O(N) 
# in worst case of unordered map, loop runs for O(N) times but searching happens in O(logN) times, so TC = O(N*logN)
def read(n: int, book: list(), target: int) -> str:
    # Write your code here.
    d = {}
    for i in range(n):
        if (target - book[i]) in d:
            return 'YES'
        else:
            d[(book[i])] = i
    return 'NO'

# Optimal Approach ( Using Two Pointer) - TC = O(N) and SC = O(1)
# first we will sort the array and take left pointer at arr[start], right at last element
# no we will check for let<right in the loop,
#  if arr[left]+arr[right] < target, then we need larger numbers so we increase left
# if arr[left]+arr[right] > target, then we need lesser numbers so we decrease right
# if arr[left]+arr[right] == target, then we need return yes.
