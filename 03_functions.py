"""
Module 01 | Part 3: Functions
=============================
Defining functions with type hints and docstrings, default/keyword
arguments, *args/**kwargs, recursion, lambdas, higher-order functions,
and a decorator.

Run:  python 03_functions.py
"""

import time
from functools import wraps
from typing import Callable, Iterable


def calculate(a: float, b: float, operation: str = "add") -> float:
    """Simple calculator. Raises on invalid operation or division by zero."""
    operations: dict[str, Callable[[float, float], float]] = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y,
    }
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation!r}")
    if operation == "div" and b == 0:
        raise ZeroDivisionError("Division by zero is undefined")
    return operations[operation](a, b)


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def is_palindrome(text: str) -> bool:
    """Case- and punctuation-insensitive palindrome check."""
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """Recursive factorial with base-case validation."""
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)


def mean(*numbers: float) -> float:
    """Arithmetic mean of any number of arguments (*args)."""
    if not numbers:
        raise ValueError("mean() requires at least one number")
    return sum(numbers) / len(numbers)


def describe_model(name: str, **hyperparameters: object) -> str:
    """Format a model description from arbitrary keyword args (**kwargs)."""
    params = ", ".join(f"{k}={v}" for k, v in sorted(hyperparameters.items()))
    return f"{name}({params})"


def apply_to_all(func: Callable, items: Iterable) -> list:
    """Higher-order function: apply `func` to every item."""
    return [func(item) for item in items]


def timer(func: Callable) -> Callable:
    """Decorator that reports how long the wrapped function takes."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[timer] {func.__name__} took {elapsed_ms:.3f} ms")
        return result
    return wrapper


@timer
def sum_of_squares(n: int) -> int:
    """Sum of squares from 1 to n."""
    return sum(i * i for i in range(1, n + 1))


def main() -> None:
    print("calculate(8, 2, 'div') =", calculate(8, 2, "div"))
    print("is_even(10) =", is_even(10), "| is_even(7) =", is_even(7))
    print("is_palindrome('A man, a plan, a canal: Panama') =",
          is_palindrome("A man, a plan, a canal: Panama"))
    print("factorial(6) =", factorial(6))
    print("mean(4, 8, 15, 16, 23, 42) =", round(mean(4, 8, 15, 16, 23, 42), 3))
    print(describe_model("RandomForest", n_estimators=200, max_depth=8))
    print("apply_to_all(len, ['ai','ml','dl']) =",
          apply_to_all(len, ["ai", "ml", "dl"]))
    print("sorted by last char:", sorted(["bat", "cab", "apple"], key=lambda w: w[-1]))
    print("sum_of_squares(100000) =", sum_of_squares(100_000))


if __name__ == "__main__":
    main()
