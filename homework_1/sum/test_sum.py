import pytest

from sum.algo import max_even_sum


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([2, 4, 6], 12),
        ([1, 2, 3], 6),
        ([8, 11, 4, 3, 9], 32),
        ([5], 0),
        ([2], 2),
        ([1, 3, 5], 8),
        ([7, 2, 4], 6),
        ([9, 4, 7, 11, 2, 8], 34),
        ([100, 1, 2], 102),
        ([1, 2], 2),
    ],
)
def test_max_even_sum(numbers, expected):
    assert max_even_sum(numbers) == expected