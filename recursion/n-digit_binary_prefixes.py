# Print N-digit Binary Number where no. of 1's >= No. of 0s is all its prefixes.

def solve(one, zero,n, output):
    if n==0:
        print(output)
        return
    
    # My solution
    # if one==zero:
    #     op1 = output+'1'
    #     solve(one+1, zero, n-1, op1)
    # if abs(one-zero)>=1:
    #     op1 = output+'1'
    #     op2 = output+'0'
    #     solve( one+1, zero, n-1, op1)
    #     solve(one, zero+1, n-1, op2)

    # Aditya Verma Solution
    op1 = output+'1'
    solve(one+1, zero, n-1, op1)
    if one>zero:
        op2 = output+'0'
        solve(one, zero+1, n-1, op2)
    return
n = 3
one, zero = 0,0
output = ''
solve(one,zero,n, output)