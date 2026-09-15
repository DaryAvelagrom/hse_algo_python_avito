import pytest

from prime.algo import count_primes


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (10, 4),
        (20, 8),
        (30, 10),
        (100, 25),
        (101, 25),
    ],
)
def test_count_primes(n, expected):
    assert count_primes(n) == expected