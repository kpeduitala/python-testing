def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def greet(name):
    return "Hello, " + name + "!"

def reverse_string(string):
    return string[::-1]

def find_max(nums):
    return max(nums)

def find_min(nums):
    return min(nums)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
