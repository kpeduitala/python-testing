# Adds two values together
def add(a, b):
    return a + b

# Subtracts second value from the first
def subtract(a, b):
    return a - b

# Multiplies two values
def multiply(a, b):
    return a * b

# Divides first value by the second (throws error if second value is 0)
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Checks if a number is even
def is_even(num):
    return num % 2 == 0

# Checks if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Greets a person with their name
def greet(name):
    return "Hello, " + name + "!"

# Reverses a given string
def reverse_string(string):
    return string[::-1]

# Finds the maximum value in a list of numbers
def find_max(nums):
    return max(nums)

# Finds the minimum value in a list of numbers
def find_min(nums):
    return min(nums)

# Counts the number of vowels in a given text
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
