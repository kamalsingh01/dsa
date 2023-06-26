# Print numbers from 1 to n using recursion

def printn(n):
    if n==1:
        print(n, end=' ')
        return
    printn(n-1)
    print(n,end =' ')

if __name__ == "__main__":
    n = int( input())
    print("Output:", end = '')
    printn(n)
    print()