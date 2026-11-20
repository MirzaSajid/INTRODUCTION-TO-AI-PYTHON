"""
Module 01 | Part 4: Lists and Core Data Structures
==================================================
List operations, slicing, sorting, and a comparison with tuples, sets
and dictionaries, plus a few common data-processing patterns.

Run:  python 04_lists_and_data_structures.py
"""

from collections import Counter


def list_basics() -> None:
    print("--- List basics ---")
    scores = [72, 88, 95, 61, 88]
    scores.append(79)                    # add to end
    scores.insert(0, 100)                # add at index
    scores.remove(61)                    # remove first matching value
    popped = scores.pop()                # remove & return last item
    print(f"scores={scores}, popped={popped}")
    print(f"len={len(scores)}, sum={sum(scores)}, max={max(scores)}, min={min(scores)}")
    print(f"sorted asc:  {sorted(scores)}")
    print(f"sorted desc: {sorted(scores, reverse=True)}")
    print(f"index of 95: {scores.index(95)}, count of 88: {scores.count(88)}")


def slicing() -> None:
    print("\n--- Slicing ---")
    data = list(range(10))
    print(f"data[2:6]   -> {data[2:6]}")
    print(f"data[:3]    -> {data[:3]}")
    print(f"data[-3:]   -> {data[-3:]}")
    print(f"data[::2]   -> {data[::2]}")
    print(f"data[::-1]  -> {data[::-1]}")


def remove_duplicates(items: list) -> list:
    """Remove duplicates while preserving the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten(nested: list[list]) -> list:
    """Flatten one level of nesting."""
    return [x for sub in nested for x in sub]


def top_n(items: list[float], n: int) -> list[float]:
    """Return the n largest values in descending order."""
    return sorted(items, reverse=True)[:n]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """Transpose a 2D list (rows <-> columns)."""
    return [list(row) for row in zip(*matrix)]


def structures_comparison() -> None:
    print("\n--- list vs tuple vs set vs dict ---")
    point = (3, 4)                                   # tuple: fixed record
    vocab = {"ai", "ml", "dl", "ai"}                 # set: unique, unordered
    student = {"name": "Ayesha", "marks": [88, 92]}  # dict: key -> value
    print(f"tuple: {point} | set (dedup): {sorted(vocab)}")
    print(f"dict lookup student['name'] = {student['name']}")
    print(f"dict.get with default: {student.get('age', 'n/a')}")

    words = "ai ml ai dl ml ai".split()
    print(f"word frequency (Counter): {dict(Counter(words))}")


def main() -> None:
    list_basics()
    slicing()
    print("\nremove_duplicates:", remove_duplicates([3, 1, 3, 2, 1, 4]))
    print("flatten:", flatten([[1, 2], [3], [4, 5]]))
    print("top_n:", top_n([5, 1, 9, 3, 7], 3))
    print("transpose:", transpose([[1, 2, 3], [4, 5, 6]]))
    structures_comparison()


if __name__ == "__main__":
    main()
