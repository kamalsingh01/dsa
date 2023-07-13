# Sort a stack usign recursion

'''
URL: https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=love-babbar-dsa-sheet-problems&leftPanelTab=0%3Fsource%3Dyoutube&campaign=Lovebabbarcodestudio
'''

from collections import deque

def insert_element(stack, element):
    if len(stack)==0 or element>=stack[-1]:
        stack.append(element)
        return
    temp = stack.pop()
    insert_element(stack, element)
    stack.append(temp)

def sort_stack(stack):
    if len(stack)==1:
        return
    element = stack.pop()
    sort_stack(stack)
    insert_element(stack, element)





if __name__ == "__main__":
    stack = deque([5,9,3,4,0,2,7,1])
    stack_size = len(stack)
    print("Original Stack: ", stack)
    sort_stack(stack)
    print("Sorted Stack: ", stack)