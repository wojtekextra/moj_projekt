import math
import pytest

from src.logic.calculator import (
    add,
    divide,
    gcd,
    is_prime,
    median,
    mode,
    power,
    prime_factors,
    root,
    solve_quadratic,
)


def test_add():
    assert add(2, 3) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_gcd():
    assert gcd(12, 18) == 6


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(1) is False


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_mode_multiple():
    assert mode([1, 2, 2, 3, 3]) == [2, 3]


def test_power():
    assert power(2, 3) == 8


def test_prime_factors():
    assert prime_factors(28) == [2, 2, 7]


def test_root_square():
    assert root(9, 2) == 3


def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (1.0, 2.0)
