# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = 5  # Change this number to test
print("Iterative:", factorial_iterative(number))
print("Recursive:", factorial_recursive(number))
