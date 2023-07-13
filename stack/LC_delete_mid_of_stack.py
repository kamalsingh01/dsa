# delete middle element of the stack
'''
URL: https://www.codingninjas.com/studio/problems/delete-middle-element-from-stack_985246?leftPanelTab=0%3Fsource%3Dyoutube&campaign=Lovebabbarcodestudio

'''
from collections import deque

# using iterative approach
def delete_mid_iterative(stack):
    lst = []
    mid = (len(stack)-1)//2
    count = len(stack)-1
    while(count!=mid):
        x = stack.pop()
        lst.append(x)
        count-=1
    stack.pop()
    count=0
    while(count<len(lst)):
        stack.append(lst[count])
        count+=1
def delete_mid_recursive(stack,count):
    if count==0:
        stack.pop()
        return 
    temp = stack.pop()
    delete_mid_recursive(stack, count-1)
    stack.append(temp)


if __name__ == "__main__":
    stack = deque([5,9,3,4,0,2,7,1])
    stack_size = len(stack)
    print("New Stack : ", stack)
    # delete_mid_iterative(stack)
    # print(" <<Iterative Approach - TC= O(n) and SC= O(n)>>")
    # print("Updated Stack : ", stack)
    mid = (len(stack)-1)//2
    count = (len(stack)-1)-mid
    delete_mid_recursive(stack, count)
    print(" <<Recursive Approach - TC= O(n) and SC= O(1)>>")
    print("Updated Stack : ", stack)
    