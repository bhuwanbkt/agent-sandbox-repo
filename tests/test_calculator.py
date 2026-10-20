from calculator import add, multiply, subtract, power


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_power() -> None:
    assert power(2, 3) == 8
    assert power(5, 0) == 1
