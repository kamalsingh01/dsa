#deleting middle element of the stack using recursion

def deleteMiddle( stack, mid):
    if mid==1:
        stack.pop()
        return
    temp = stack[-1]
    stack.pop()
    deleteMiddle(stack,mid-1)
    stack.append(temp)


if __name__ == "__main__":
    stack = []
    n = int(input(" Enter number of elements in stack: "))
    if n==0:
        print("Stack Empty")
        exit()
    print("Enter the elements: ")
    for i in range(n):
        stack.append( int(input()) )
    mid = (n//2)+1
    deleteMiddle(stack, mid)
    print("Updated Stack :", stack)