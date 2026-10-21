"""A tiny calculator used as the agent's practice repository.

Provides basic arithmetic functions and a simple expression parser.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def _tokenize(text: str):
    """Split a space‑separated expression into numbers and operators.

    Returns a list where numeric literals are converted to ``float`` and
    operators are kept as strings. Raises ``ValueError`` if an unknown token
    is encountered.
    """
    if not text:
        raise ValueError("Empty expression")
    tokens = []
    for part in text.split():
        if part in {"+", "-", "*", "/"}:
            tokens.append(part)
        else:
            try:
                tokens.append(float(part))
            except Exception as exc:
                raise ValueError(f"Invalid token: {part}") from exc
    return tokens


def parse_expression(text: str) -> float:
    """Parse and evaluate a simple arithmetic expression.

    The expression must be *space‑separated* and may contain the operators
    ``+``, ``-``, ``*`` and ``/`` together with numeric literals. Operator
    precedence follows the usual rules: ``*`` and ``/`` are evaluated before
    ``+`` and ``-``. All operations are left‑associative.

    Example
    -------
    >>> parse_expression('2 + 3 * 4')
    14.0
    """
    tokens = _tokenize(text)
    # First pass: handle * and /
    i = 0
    new_tokens = []
    while i < len(tokens):
        token = tokens[i]
        if token == "*" or token == "/":
            if not new_tokens:
                raise ValueError("Operator at start of expression")
            left = new_tokens.pop()
            # Next token must be a number
            if i + 1 >= len(tokens) or not isinstance(tokens[i + 1], (int, float)):
                raise ValueError("Missing right operand for operator")
            right = tokens[i + 1]
            result = left * right if token == "*" else left / right
            new_tokens.append(result)
            i += 2
        else:
            new_tokens.append(token)
            i += 1
    # Second pass: handle + and -
    if not new_tokens:
        raise ValueError("Empty expression after tokenisation")
    result = new_tokens[0]
    i = 1
    while i < len(new_tokens):
        op = new_tokens[i]
        if i + 1 >= len(new_tokens):
            raise ValueError("Trailing operator")
        num = new_tokens[i + 1]
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        else:
            raise ValueError(f"Unexpected operator {op}")
        i += 2
    return float(result)
