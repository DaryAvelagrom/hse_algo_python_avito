from random import Random

import pytest

from homework_7.k_th_minheap.algo import kth_largest, kth_largest_heapq


@pytest.fixture(params=[kth_largest, kth_largest_heapq])
def find(request):
    return request.param


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7], 1, 7),
        ([5] * 20, 10, 5),
        ([-5, -1, -4, -2, -1], 1, -1),
        ([-5, -1, -4, -2, -1], 5, -5),
    ],
)
def test_examples(find, nums, k, expected):
    original = nums.copy()
    assert find(nums, k) == expected
    assert nums == original


def test_all_ranks(find):
    nums = Random(7).choices(range(-20, 21), k=100)
    for k, expected in enumerate(sorted(nums, reverse=True), start=1):
        assert find(nums, k) == expected


@pytest.mark.parametrize("nums, k", [([], 1), ([1, 2], 0), ([1, 2], -1), ([1, 2], 3)])
def test_invalid_rank(find, nums, k):
    with pytest.raises(ValueError):
        find(nums, k)
