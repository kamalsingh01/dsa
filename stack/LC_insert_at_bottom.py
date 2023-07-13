# Insert an element at the bottom of the stack

'''
URL : https://www.codingninjas.com/studio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166?topList=love-babbar-dsa-sheet-problems&leftPanelTab=0%3Fsource%3Dyoutube&campaign=Lovebabbarcodestudio
'''

from collections import deque


def insert_at_bottom(stack, element):
    if len(stack)==0:
        stack.append(element)
        return
    temp = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(temp)

if __name__ == "__main__":
    stack = deque( [5,7,1,2])
    element = 9
    print("Original stack: ", stack)
    insert_at_bottom(stack, element)
    print("Updated Stack: ", stack)