"""A tiny calculator used as the agent's practice repository."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def multiply_n(*numbers: float) -> float:
    """Return the product of an arbitrary number of numbers.

    If no arguments are provided, the function returns ``1`` – the multiplicative
    identity. This mirrors the behaviour of ``math.prod`` in the standard library
    and makes the function safe to use in reductions.
    """
    product = 1.0
    for n in numbers:
        product *= n
    return product
