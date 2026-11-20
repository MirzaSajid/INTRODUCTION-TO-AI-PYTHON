"""
Module 01 | Part 5: Mini Program - Student Grade Analyzer
=========================================================
A complete beginner-to-intermediate program that combines variables,
loops, functions, lists and dictionaries. It computes descriptive
statistics (mean, median, standard deviation), assigns grades, ranks
students, and flags outliers using the z-score: a first taste of the
data analysis that underpins machine learning.

Run:  python 05_student_grade_analyzer.py
"""

import math
from statistics import median

STUDENTS: dict[str, list[float]] = {
    "Ayesha": [88, 92, 79, 95],
    "Bilal":  [65, 70, 58, 72],
    "Chen":   [91, 89, 94, 97],
    "Diana":  [45, 52, 60, 48],
    "Elif":   [77, 81, 85, 80],
}


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def std_dev(values: list[float]) -> float:
    """Population standard deviation."""
    mu = mean(values)
    return math.sqrt(sum((v - mu) ** 2 for v in values) / len(values))


def letter_grade(avg: float) -> str:
    for cutoff, grade in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if avg >= cutoff:
            return grade
    return "F"


def analyze(students: dict[str, list[float]]) -> list[dict]:
    """Return one summary record per student, ranked by average."""
    records = []
    for name, marks in students.items():
        avg = mean(marks)
        records.append({
            "name": name,
            "average": round(avg, 2),
            "best": max(marks),
            "worst": min(marks),
            "grade": letter_grade(avg),
        })
    records.sort(key=lambda r: r["average"], reverse=True)
    for rank, rec in enumerate(records, start=1):
        rec["rank"] = rank
    return records


def find_outliers(records: list[dict], threshold: float = 1.5) -> list[str]:
    """Flag students whose average is > `threshold` std devs from the class mean."""
    averages = [r["average"] for r in records]
    mu, sigma = mean(averages), std_dev(averages)
    if sigma == 0:
        return []
    return [r["name"] for r in records if abs((r["average"] - mu) / sigma) > threshold]


def print_report(records: list[dict]) -> None:
    header = f"{'Rank':<5}{'Name':<10}{'Avg':>8}{'Best':>7}{'Worst':>7}{'Grade':>7}"
    print(header)
    print("-" * len(header))
    for r in records:
        print(f"{r['rank']:<5}{r['name']:<10}{r['average']:>8.2f}"
              f"{r['best']:>7.0f}{r['worst']:>7.0f}{r['grade']:>7}")


def main() -> None:
    records = analyze(STUDENTS)
    print_report(records)

    averages = [r["average"] for r in records]
    print("\nClass statistics")
    print(f"  Mean:    {mean(averages):.2f}")
    print(f"  Median:  {median(averages):.2f}")
    print(f"  Std dev: {std_dev(averages):.2f}")
    print(f"  Outliers (|z| > 1.5): {find_outliers(records) or 'none'}")


if __name__ == "__main__":
    main()
