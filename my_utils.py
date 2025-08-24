def greet(name):
    return f"Hello, {name}! Welcome to my_utils.py! This module contains utility functions for various tasks."

    def add(a, b):
        return a + b
    
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)