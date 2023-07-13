from collections import deque

def reverese_string(string):
    stack = deque()
    for i in string:
        stack.append(i)
    string = ''
    for i in range(len(stack)):
        string += stack.pop()
    return string

if __name__ == "__main__":
    string = input("Enter the string: ")
    print("Reversed String: ", reverese_string(string))