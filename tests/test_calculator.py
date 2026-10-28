from calculator import add, multiply, subtract, multiply_n


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_multiply_n_multiple() -> None:
    assert multiply_n(2, 3, 4) == 24


def test_multiply_n_single() -> None:
    assert multiply_n(5) == 5


def test_multiply_n_empty() -> None:
    assert multiply_n() == 1
