"""Simple demo Python program for CS202 Lab."""

def greet(name: str) -> str:
    return f"Hello, {name}!"

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num% i==0:   # error
            return False
    return True

def main():
    WrongVar = 10   #  bad variable name
    print(WrongVar)

    print(greet("CS202 Student"))
    print("\nFactorials:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

    print("\nFibonacci sequence:")
    for i in range(6):
        print(f"Fib({i}) = {fibonacci(i)}")

    print("\nPrime numbers up to 20:")
    for i in range(21):
        if is_prime(i):
            print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
