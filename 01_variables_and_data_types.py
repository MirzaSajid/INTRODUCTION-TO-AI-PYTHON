"""
Module 01 | Part 1: Variables and Data Types
=============================================
Demonstrates Python's core built-in types, type conversion, string
formatting, and basic operators using a small AI-flavoured example
(describing a machine learning model run).

Run:  python 01_variables_and_data_types.py
"""


def demo_core_types() -> None:
    """Show the primary built-in types and inspect them with type()."""
    model_name = "LinearRegression"      # str
    epochs = 100                         # int
    learning_rate = 0.01                 # float
    is_trained = False                   # bool
    best_score = None                    # NoneType (value not yet available)

    print("--- Core types ---")
    for label, value in [
        ("model_name", model_name),
        ("epochs", epochs),
        ("learning_rate", learning_rate),
        ("is_trained", is_trained),
        ("best_score", best_score),
    ]:
        print(f"{label:<14} = {value!r:<18} -> {type(value).__name__}")


def demo_type_conversion() -> None:
    """Explicit (casting) and implicit type conversion."""
    print("\n--- Type conversion ---")
    raw_input_value = "42"               # data from a file or user is often str
    as_int = int(raw_input_value)
    as_float = float(raw_input_value)
    print(f"str -> int:   {raw_input_value!r} -> {as_int}")
    print(f"str -> float: {raw_input_value!r} -> {as_float}")

    # Implicit conversion: int + float is promoted to float
    print(f"Implicit promotion: 3 + 0.5 = {3 + 0.5} ({type(3 + 0.5).__name__})")

    # Conversion can fail; handle it instead of crashing
    try:
        int("forty-two")
    except ValueError as err:
        print(f"Invalid conversion handled safely: {err}")


def demo_operators() -> None:
    """Arithmetic, comparison, and logical operators."""
    print("\n--- Operators ---")
    a, b = 17, 5
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b:.3f}   (true division)")
    print(f"{a} // {b} = {a // b}       (floor division)")
    print(f"{a} % {b} = {a % b}        (modulo)")
    print(f"{a} ** {b} = {a ** b}  (power)")
    print(f"Chained comparison 0 < {b} < 10 -> {0 < b < 10}")
    print(f"Logical: ({a} > 10) and ({b} > 10) -> {(a > 10) and (b > 10)}")


def demo_strings() -> None:
    """Common string operations and f-string formatting."""
    print("\n--- Strings ---")
    text = "  Artificial Intelligence  "
    print(f"strip():   {text.strip()!r}")
    print(f"upper():   {text.strip().upper()}")
    print(f"split():   {text.split()}")
    print(f"replace(): {text.strip().replace('Artificial', 'Applied')}")
    accuracy = 0.93847
    print(f"Formatted: accuracy = {accuracy:.2%}")   # 93.85%


def demo_mutability() -> None:
    """Mutable vs immutable types: a classic source of bugs."""
    print("\n--- Mutability ---")
    t = (1, 2, 3)                 # tuple: immutable
    l = [1, 2, 3]                 # list: mutable
    l[0] = 99
    print(f"list after change:  {l}")
    try:
        t[0] = 99                 # type: ignore[index]
    except TypeError as err:
        print(f"tuple cannot change: {err}")

    alias = l                     # both names point to the SAME object
    alias.append(4)
    print(f"alias effect on original list: {l}")
    independent = l.copy()        # a real copy
    independent.append(5)
    print(f"original unchanged after copy: {l}")


def main() -> None:
    demo_core_types()
    demo_type_conversion()
    demo_operators()
    demo_strings()
    demo_mutability()


if __name__ == "__main__":
    main()
