from random import Random

import pytest

from homework_6.k_th.algo import kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7], 1, 7),
        ([2] * 1500, 750, 2),
        ([-4, 0, -9, -4], 1, 0),
        ([-4, 0, -9, -4], 4, -9),
    ],
)
def test_examples(nums, k, expected):
    original = nums.copy()
    assert kth_largest(nums, k) == expected
    assert nums == original


def test_all_ranks():
    nums = Random(6).choices(range(-20, 21), k=101)
    for k, expected in enumerate(sorted(nums, reverse=True), start=1):
        assert kth_largest(nums, k) == expected


@pytest.mark.parametrize("nums, k", [([], 1), ([1, 2], 0), ([1, 2], -1), ([1, 2], 3)])
def test_invalid_rank(nums, k):
    with pytest.raises(ValueError):
        kth_largest(nums, k)
