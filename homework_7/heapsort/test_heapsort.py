from random import Random

import pytest

from homework_7.heapsort.algo import heapsort


@pytest.mark.parametrize(
    "values",
    [
        [], [7], [2, 1], [4, 1, 4, -2, 0, 3, -2], [5] * 16,
        list(range(1000)), list(range(1025, 0, -1)),
        Random(7).choices(range(-100, 101), k=500),
    ],
)
def test_heapsort(values):
    arr = values.copy()
    alias = arr
    assert heapsort(arr) is alias
    assert alias == sorted(values)
