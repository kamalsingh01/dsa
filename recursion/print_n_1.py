# Print numbers from n to 1 using recursion

def printn(n):
    if n==1:
        print(n, end=' ')
        return
    print(n,end =' ')
    printn(n-1)
    

if __name__ == "__main__":
    n = int( input())
    print("Output:", end = '')
    printn(n)
    print()