#finds factorial of the given number using recursion

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

# here is the main function
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"Factorial of {n} is ", factorial(n))