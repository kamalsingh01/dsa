def subset(ip, output, s):
    if ip =='':             # base condition
        s.add(output)       # sxet only keeps unique subsets
        return 
    op1 = output           # for left-side
    op2 = output+ip[0]     # for right-side
    ip = ip[1:]
    subset(ip,op1,s)
    subset(ip,op2,s)

string = "aac"
output = ""
s = set()
subset(string, output,s)
print(s)