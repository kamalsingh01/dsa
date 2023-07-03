def solve(string, output):
    if string == '':
        print(output)
        return
    output1 = output+ string[0]
    output2 = output+string[0].upper()
    string = string[1:]
    solve(string, output1)
    solve(string, output2)
    return

string = "abc"
output = '' 
solve(string, output)