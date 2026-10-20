"""A tiny calculator used as the agent's practice repository."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def power(base: float, exponent: float) -> float:
    """Return base raised to the exponent using the ``**`` operator.

    This mirrors the behavior of Python's exponentiation and works for
    both integer and floating‑point values.
    """
    return base ** exponent
