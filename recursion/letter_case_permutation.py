def solve(string, output):
    if string=='':
        print(output)
        return
    if string[0].isdigit():
        output = output+string[0]     
        op1=output
        string = string[1:]
    if string!='':
        if string[0].isalpha():
            op1 = output+string[0].lower()
            op2 = output+string[0].upper()
            string = string[1:]
            solve(string, op1)
            solve(string, op2)
    else:
        solve(string, op1)  # keep an eye here, as we have only 1 choice, 1 is included in both the choices of A,
                        # so we add 1 in output and make a single call for that output, again further choice is made for letter.
    return


string = 'a1B2'
output =''
solve(string,output)