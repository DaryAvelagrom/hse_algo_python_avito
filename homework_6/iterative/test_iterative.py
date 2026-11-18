from random import Random

import pytest

from homework_6.iterative.algo import mergesort, quicksort


@pytest.mark.parametrize("sort", [mergesort, quicksort])
@pytest.mark.parametrize(
    "nums",
    [
        [], [7], [2, 1], [4, 1, 4, -2, 0, 3, -2],
        list(range(1200)), list(range(1200, 0, -1)), [7] * 1200,
        Random(6).choices(range(-20, 21), k=257),
    ],
)
def test_sort(sort, nums):
    original = nums.copy()
    assert sort(nums) == sorted(original)
    assert nums == original
