"""A tiny calculator used as the agent's practice repository."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def modulo(a: float, b: float) -> float:
    """Return a modulo b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero")
    return a % b
