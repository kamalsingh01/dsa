#deleting middle element of the stack using recursion

# we can also decrease mid at every recursion call and make base condition as
'''
def deleteMiddle( stack, mid):
    if mid==1:
        stack.pop()
        return
    temp = stack.pop()
    deleteMiddle(stack,mid-1)
    stack.append(temp)
        
'''

def deleteMiddle( stack, mid):
    if mid==len(stack):
        stack.pop()
        return
    temp = stack.pop()
    deleteMiddle(stack,mid)
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
    mid = (len(stack)//2)+1
    deleteMiddle(stack, mid)
    print("Updated Stack :", stack)