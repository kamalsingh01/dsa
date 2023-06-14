def generate_parenthesis(open,close,output):
    if open == 0 and close == 0:
        print(output)
        return
 
    if open!=0:
        op1 = output + '('  #for open
        generate_parenthesis(open-1, close, op1)
    if close>open:
        op2 = output + ')'  #for closed
        generate_parenthesis(open, close-1, op2 )   #for close

if __name__ == "__main__":
    n = int(input("Enter number of Parenthesis: "))
    if n>1:
        output = ''
        generate_parenthesis(n,n,output)
    else:
        print("no parenthesis involved")


# number of pattersn( catalan number) : (2n)! / ( (n+1)!.n!)