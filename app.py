"""Simple demo Python program for CS202 Lab."""

def greet(name: str) -> str:
    return f"Hello, {name}!"

def factorial(n: int) -> int:
    """Return factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Return nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(num: int) -> bool:
    """Check if num is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main() -> None:
    """Demo of functions."""
    demo_var = 10
    print(demo_var)
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
