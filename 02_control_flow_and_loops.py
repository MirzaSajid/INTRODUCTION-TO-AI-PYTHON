"""
Module 01 | Part 2: Control Flow and Loops
==========================================
Conditionals, for/while loops, comprehensions, and loop control
(break / continue / else). Includes classic algorithmic exercises.

Run:  python 02_control_flow_and_loops.py
"""


def classify_score(score: float) -> str:
    """Map a numeric score to a letter grade using if/elif/else."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def multiplication_table(n: int, upto: int = 10) -> None:
    """Print the multiplication table of n with a for loop."""
    print(f"\nMultiplication table of {n}")
    for i in range(1, upto + 1):
        print(f"{n} x {i:>2} = {n * i:>3}")


def triangle_pattern(rows: int) -> None:
    """Print a right-aligned triangle using nested loops."""
    print("\nTriangle pattern")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


def fibonacci(limit: int) -> list[int]:
    """Return Fibonacci numbers not exceeding `limit` (while loop)."""
    sequence, a, b = [], 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence


def primes_up_to(n: int) -> list[int]:
    """Sieve of Eratosthenes: efficient prime generation, O(n log log n)."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [i for i, flag in enumerate(is_prime) if flag]


def first_negative(values: list[float]) -> float | None:
    """Demonstrate break and for-else: find the first negative value."""
    for v in values:
        if v < 0:
            found = v
            break
    else:                        # runs only if the loop was NOT broken
        return None
    return found


def collatz_steps(n: int) -> int:
    """Number of steps for n to reach 1 in the Collatz sequence."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def comprehension_examples() -> None:
    """List, dict and set comprehensions: concise, Pythonic loops."""
    print("\nComprehensions")
    squares = [x ** 2 for x in range(1, 8)]
    evens = [x for x in range(20) if x % 2 == 0]
    square_map = {x: x ** 2 for x in range(1, 5)}
    unique_lengths = {len(w) for w in ["ai", "ml", "deep", "learning"]}
    print(f"squares: {squares}")
    print(f"evens: {evens}")
    print(f"square_map: {square_map}")
    print(f"unique_lengths: {unique_lengths}")


def main() -> None:
    for s in (95, 83.5, 71, 64, 20):
        print(f"Score {s:>5} -> Grade {classify_score(s)}")
    multiplication_table(7, 5)
    triangle_pattern(4)
    print(f"\nFibonacci <= 100: {fibonacci(100)}")
    print(f"Primes <= 50:     {primes_up_to(50)}")
    print(f"First negative:   {first_negative([3, 8, -2, 5, -9])}")
    print(f"No negatives:     {first_negative([1, 2, 3])}")
    print(f"Collatz(27) steps: {collatz_steps(27)}")
    comprehension_examples()


if __name__ == "__main__":
    main()
