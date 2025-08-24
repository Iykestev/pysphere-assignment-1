import my_utils

def main():
    #using custom utility functions from my_utils.py
    name = "Alice"
    print(my_utils.greet(name))

    #using the add function
    a, b = 5, 10
    print(f"The sum of {a} and {b} is: {my_utils.add(a, b)}")

    #using the factorial function
    n = 5
    print(f"The factorial of {n} is: {my_utils.factorial(n)}")

    if __name__ == "__main__":
        main()



