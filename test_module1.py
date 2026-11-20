"""Unit tests for Module 01. Run from the repo root:  python -m unittest discover -s tests -v"""

import importlib
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

loops = importlib.import_module("02_control_flow_and_loops")
funcs = importlib.import_module("03_functions")
lists = importlib.import_module("04_lists_and_data_structures")
analyzer = importlib.import_module("05_student_grade_analyzer")
ml = importlib.import_module("06_ml_intro_linear_regression")


class TestLoops(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(loops.classify_score(95), "A")
        self.assertEqual(loops.classify_score(59.9), "F")
        with self.assertRaises(ValueError):
            loops.classify_score(101)

    def test_fibonacci(self):
        self.assertEqual(loops.fibonacci(20), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_primes(self):
        self.assertEqual(loops.primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(loops.primes_up_to(1), [])

    def test_first_negative(self):
        self.assertEqual(loops.first_negative([1, -4, -2]), -4)
        self.assertIsNone(loops.first_negative([1, 2]))

    def test_collatz(self):
        self.assertEqual(loops.collatz_steps(27), 111)


class TestFunctions(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(funcs.calculate(6, 3, "mul"), 18)
        with self.assertRaises(ZeroDivisionError):
            funcs.calculate(1, 0, "div")
        with self.assertRaises(ValueError):
            funcs.calculate(1, 2, "pow")

    def test_palindrome(self):
        self.assertTrue(funcs.is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(funcs.is_palindrome("machine learning"))

    def test_factorial(self):
        self.assertEqual(funcs.factorial(5), 120)
        with self.assertRaises(ValueError):
            funcs.factorial(-1)

    def test_mean_and_kwargs(self):
        self.assertAlmostEqual(funcs.mean(1, 2, 3, 4), 2.5)
        self.assertEqual(funcs.describe_model("M", b=2, a=1), "M(a=1, b=2)")


class TestLists(unittest.TestCase):
    def test_remove_duplicates_keeps_order(self):
        self.assertEqual(lists.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_flatten_top_transpose(self):
        self.assertEqual(lists.flatten([[1], [2, 3]]), [1, 2, 3])
        self.assertEqual(lists.top_n([4, 9, 1], 2), [9, 4])
        self.assertEqual(lists.transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])


class TestAnalyzer(unittest.TestCase):
    def test_ranking_and_grade(self):
        records = analyzer.analyze(analyzer.STUDENTS)
        self.assertEqual(records[0]["name"], "Chen")
        self.assertEqual(records[0]["rank"], 1)
        self.assertEqual(records[0]["grade"], "A")

    def test_std_dev(self):
        self.assertAlmostEqual(analyzer.std_dev([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)


class TestLinearRegression(unittest.TestCase):
    def test_model_learns_relationship(self):
        X, y = ml.make_dataset()
        model = ml.LinearRegression(learning_rate=0.01, epochs=3000).fit(X, y)
        self.assertAlmostEqual(model.w, 5, delta=0.6)
        self.assertGreater(model.score(X, y), 0.9)
        self.assertLess(model.loss_history[-1], model.loss_history[0])


if __name__ == "__main__":
    unittest.main()
