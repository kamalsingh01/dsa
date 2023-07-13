# Check if any redundant bracket(s) are present in a a string

'''

''' 

from collections import deque

def check(string):
    stack=[]
    for i in string:
        if i in ['(','+','-','*','/']:
            stack.append(i)
        else:
            if i == ')':
                isredun = True
                if len(stack)>0:
                    top = stack[-1]
                    while( top != '(' ):
                        if top in ['+','-','*','/']:
                            isredun = False
                            stack.pop()
                    if isredun ==True:
                        return 'Yes'
                    stack.pop()
    return "No"

if __name__ == "__main__":
    string = "((a*b)+c)"
    print(check(string))
