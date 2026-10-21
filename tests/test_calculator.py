from calculator import add, multiply, subtract, modulo


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_modulo() -> None:
    assert modulo(10, 3) == 1


def test_modulo_zero_divisor() -> None:
    import pytest
    with pytest.raises(ValueError):
        modulo(5, 0)
