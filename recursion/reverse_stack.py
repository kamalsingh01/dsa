#reversing a stack using recursion - Uses SC = O(1)

def reverseStack(stack):
    if len(stack) == 1:
        return
    element = stack[-1]
    stack.pop()
    reverseStack(stack)
    insert(stack, element)
    
def insert(stack, element):
    if len(stack)==0:
        stack.append(element)
        return
    temp = stack[-1]
    stack.pop()
    insert(stack, element)      # keep an eye on this stage, we are placing element on the last, but we are popping temp for the process and we will append it back once element is placed.
    stack.append(temp)


if __name__ == "__main__":
    stack = [2,3,4,5,6]
    # n = int(input(" Enter number of elements in stack: "))
    # if n==0:
    #     print("Stack Empty")
    #     exit()
    # print("Enter the elements: ")
    # for i in range(n):
    #     stack.append( int(input()) )
    reverseStack(stack)
    print("Reversed Stack :", stack)