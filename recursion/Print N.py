def print_n( n ):
    if n==0:
        return
    
    print(n)
    print_n (n-1)


n = int(input())
print_n(n)