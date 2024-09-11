# Recursive function to return Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to print the Fibonacci series up to 'n' terms
def print_fibonacci_series(n):
    print(f"Fibonacci series for {n} terms:")
    for i in range(n):
        print(fibonacci(i), end=" ")

# Input number of terms
terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print_fibonacci_series(terms)
