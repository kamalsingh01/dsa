def sum_first(n):
    if n==1:
        return 1
    return n+sum_first(n-1)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(" Sum of first",n,"natural numbers: ", sum_first(n))