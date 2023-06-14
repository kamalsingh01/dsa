def print_subset(string, output):
    if len(string)==0:  #when input becomes '', print ther output produced at leaf node.
        print(output)
        return
    op1 = output
    op2 = output + string[0]
    inp = string[1:]
    print_subset(inp, op1)
    print_subset(inp, op2)

if __name__ == "__main__":
    string = input("Enter the string: ")
    output = ""
    print_subset(string, output)