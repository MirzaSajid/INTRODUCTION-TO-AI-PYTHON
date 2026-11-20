# AI & Python: Module 01

Foundations of Artificial Intelligence, Machine Learning and Python programming.
This repository contains all Module 01 deliverables (Days 1 to 4): clean, tested
Python code covering the core language, plus a from-scratch machine learning
example that bridges programming and AI.

## Learning Objectives Covered

| # | Objective | Where |
|---|-----------|-------|
| 1 | Basics of Artificial Intelligence and Machine Learning | `06_ml_intro_linear_regression.py`, Learning Notes |
| 2 | Difference between AI, ML and Deep Learning | Learning Notes |
| 3 | Real-world AI applications | Learning Notes |
| 4 | Python concepts: variables, loops, functions, lists | `01` to `04` |
| 5 | Beginner-friendly Python programs | `05`, `06` |

## Repository Structure

```
ai-python-module-1/
├── 01_variables_and_data_types.py      # types, casting, operators, strings, mutability
├── 02_control_flow_and_loops.py        # if/elif, for/while, sieve of Eratosthenes, comprehensions
├── 03_functions.py                     # type hints, *args/**kwargs, recursion, decorators
├── 04_lists_and_data_structures.py     # lists, slicing, sets, dicts, Counter
├── 05_student_grade_analyzer.py        # mini program: statistics, ranking, z-score outliers
├── 06_ml_intro_linear_regression.py    # linear regression + gradient descent, no libraries
├── tests/test_module1.py               # 14 unit tests
├── .gitignore
└── README.md
```

## Requirements

Python 3.10 or newer. No third-party packages; everything uses the standard library.

## How to Run

```bash
git clone https://github.com/<your-username>/ai-python-module-1.git
cd ai-python-module-1

python 01_variables_and_data_types.py
python 05_student_grade_analyzer.py
python 06_ml_intro_linear_regression.py

# Run the test suite
python -m unittest discover -s tests -v
```

## Highlights

### Student Grade Analyzer (`05`)
Combines functions, lists, dictionaries and loops to rank students, assign
grades and flag statistical outliers using z-scores.

```
Rank Name           Avg   Best  Worst  Grade
1    Chen         92.75     97     89      A
2    Ayesha       88.50     95     79      B
...
Outliers (|z| > 1.5): ['Diana']
```

### Linear Regression from Scratch (`06`)
A model implemented in pure Python that learns `y = w*x + b` through gradient
descent on Mean Squared Error, evaluated on a held-out test set. This is the
same optimisation principle used to train deep neural networks.

```
Learned parameters: w = 5.108 (true 5), b = 39.652 (true 40)
Loss: start 4501.85 -> end 6.15
R^2 train: 0.973
R^2 test:  0.967
```

## Key Takeaways

- Writing readable code: type hints, docstrings, small single-purpose functions.
- Handling errors explicitly instead of letting programs crash.
- Verifying behaviour with unit tests.
- Machine learning is optimisation: define a model, a loss, and minimise it.

## Author

Sajid Hussain | Module 01, AI & Python Program
