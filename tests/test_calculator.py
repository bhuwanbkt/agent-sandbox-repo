from calculator import add, multiply, subtract, divide


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_divide() -> None:
    assert divide(10, 2) == 5


def test_divide_by_zero() -> None:
    import pytest
    with pytest.raises(ValueError):
        divide(5, 0)
