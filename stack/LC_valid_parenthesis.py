# Check if the string contains valid parenthesis
'''
URL : https://www.codingninjas.com/studio/problems/valid-parenthesis_795104?topList=love-babbar-dsa-sheet-problems&leftPanelTab=1&campaign=Lovebabbarcodestudio
'''

from collections import deque

def check_valid_parenthesis(string):
    stack = deque()
    for i in string:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if len(stack)>0:
                if stack[-1]=='(' and i==')':
                    stack.pop()
                elif stack[-1]=='{' and i=='}':
                    stack.pop()
                elif stack[-1]=='[' and i==']':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack)==0:
        return True


if __name__ == "__main__":
    string = "{([(]])}"
    if check_valid_parenthesis(string):
        print(" Valid Parenthesis")
    else:
        print(" Not a valid parenthesis")