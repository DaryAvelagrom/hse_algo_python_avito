from random import Random

import pytest

from homework_6.compare.algo import compare_times, measure_time, mergesort, quicksort


@pytest.mark.parametrize("sort", [mergesort, quicksort])
@pytest.mark.parametrize(
    "nums",
    [
        [], [7], [3, -1, 3, 0, -2, 5, 3],
        list(range(1500)), list(range(1500, 0, -1)), [7] * 1500,
        Random(6).sample(range(-1000, 1000), 301),
    ],
)
def test_sort(sort, nums):
    original = nums.copy()
    assert sort(nums) == sorted(original)
    assert nums == original


def test_measure_time():
    @measure_time
    def multiply(value, *, factor):
        return value * factor

    result, elapsed = multiply(3, factor=4)
    assert result == 12
    assert elapsed >= 0
    assert multiply.__name__ == "multiply"


def test_compare_times():
    times = compare_times([3, 1, 2], repeats=3)
    assert times.keys() == {"mergesort", "quicksort"}
    assert all(elapsed >= 0 for elapsed in times.values())
