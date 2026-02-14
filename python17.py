 # Factorial of Large Number

def factorialDigits(n):
    result = 1
    
    for i in range(2, n + 1):
        result *= i
    
    # Convert number into list of digits
    return list(map(int, str(result)))


# Example 1
print(factorialDigits(5))

# Example 2
print(factorialDigits(10))

# Example 3
print(factorialDigits(1))
