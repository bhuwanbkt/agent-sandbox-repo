from calculator import add, multiply, subtract, parse_expression


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_precedence() -> None:
    assert parse_expression('2 + 3 * 4') == 14.0


def test_left_to_right() -> None:
    # 10 - 5 - 2 should be (10 - 5) - 2 = 3
    assert parse_expression('10 - 5 - 2') == 3.0


def test_division() -> None:
    # 8 / 2 * 3 should be (8 / 2) * 3 = 12
    assert parse_expression('8 / 2 * 3') == 12.0


def test_zero_division() -> None:
    import pytest
    with pytest.raises(ZeroDivisionError):
        parse_expression('5 / 0')


def test_invalid_token() -> None:
    import pytest
    with pytest.raises(ValueError):
        parse_expression('2 + a')
