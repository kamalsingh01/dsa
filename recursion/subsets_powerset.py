# PRIINT ALL SUBSET / PRINT POWERSET

def subset(ip, output):
    if ip =='':      # base condition
        print(output)
        return 
    op1 = output           # for left-side
    op2 = output+ip[0]     # for right-side
    ip = ip[1:]
    subset(ip,op1)
    subset(ip,op2)

string = "abc"
output = ""
subset(string, output)