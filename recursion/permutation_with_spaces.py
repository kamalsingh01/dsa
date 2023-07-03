def solve(string, output):
    if string == '':
        print(output)
        return
    output1 = output+string[0]
    output2 = output+"_"+string[0]
    string = string[1:]
    solve(string, output1)
    solve(string, output2)
    return

string = "ABC"
output = ''
# since we have no choice for A, so we append A in output itself
output = output+string[0]
string = string[1:]
solve(string, output)