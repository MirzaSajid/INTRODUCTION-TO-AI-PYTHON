"""
Module 01 | Part 6: ML Preview - Linear Regression from Scratch
===============================================================
Machine learning in its simplest form, implemented in pure Python with
no libraries. The model learns y = w*x + b from data using gradient
descent, which is the same optimisation idea that trains deep neural
networks.

Problem: predict exam score from hours studied.

Run:  python 06_ml_intro_linear_regression.py
"""

import random


class LinearRegression:
    """Single-feature linear regression trained with gradient descent."""

    def __init__(self, learning_rate: float = 0.01, epochs: int = 2000):
        self.lr = learning_rate
        self.epochs = epochs
        self.w = 0.0          # weight (slope)
        self.b = 0.0          # bias (intercept)
        self.loss_history: list[float] = []

    def predict(self, x: float) -> float:
        return self.w * x + self.b

    def fit(self, X: list[float], y: list[float]) -> "LinearRegression":
        n = len(X)
        for _ in range(self.epochs):
            preds = [self.predict(x) for x in X]
            errors = [p - t for p, t in zip(preds, y)]
            # Gradients of Mean Squared Error w.r.t. w and b
            dw = (2 / n) * sum(e * x for e, x in zip(errors, X))
            db = (2 / n) * sum(errors)
            self.w -= self.lr * dw
            self.b -= self.lr * db
            self.loss_history.append(sum(e * e for e in errors) / n)
        return self

    def score(self, X: list[float], y: list[float]) -> float:
        """R-squared: proportion of variance explained by the model."""
        mean_y = sum(y) / len(y)
        ss_res = sum((t - self.predict(x)) ** 2 for x, t in zip(X, y))
        ss_tot = sum((t - mean_y) ** 2 for t in y)
        return 1 - ss_res / ss_tot


def make_dataset(n: int = 40, seed: int = 42) -> tuple[list[float], list[float]]:
    """Synthetic data: score = 5*hours + 40 + noise."""
    rng = random.Random(seed)
    X = [rng.uniform(0, 10) for _ in range(n)]
    y = [5 * x + 40 + rng.gauss(0, 3) for x in X]
    return X, y


def train_test_split(X, y, test_ratio: float = 0.25, seed: int = 0):
    idx = list(range(len(X)))
    random.Random(seed).shuffle(idx)
    cut = int(len(X) * (1 - test_ratio))
    tr, te = idx[:cut], idx[cut:]
    return ([X[i] for i in tr], [y[i] for i in tr],
            [X[i] for i in te], [y[i] for i in te])


def main() -> None:
    X, y = make_dataset()
    X_train, y_train, X_test, y_test = train_test_split(X, y)

    model = LinearRegression(learning_rate=0.01, epochs=3000).fit(X_train, y_train)

    print(f"Learned parameters: w = {model.w:.3f} (true 5), b = {model.b:.3f} (true 40)")
    print(f"Loss: start {model.loss_history[0]:.2f} -> end {model.loss_history[-1]:.2f}")
    print(f"R^2 train: {model.score(X_train, y_train):.3f}")
    print(f"R^2 test:  {model.score(X_test, y_test):.3f}   (generalisation)")
    for hours in (2, 5, 8):
        print(f"Predicted score for {hours}h study: {model.predict(hours):.1f}")


if __name__ == "__main__":
    main()
