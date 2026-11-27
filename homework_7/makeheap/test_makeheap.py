from random import Random

import pytest

from homework_7.makeheap.algo import makeheap, makeheap_n_log_n


@pytest.mark.parametrize("build", [makeheap, makeheap_n_log_n])
@pytest.mark.parametrize(
    "values",
    [
        [], [7], [2, 1], [4, 1, 4, -2, 0, 3, -2], [5] * 16,
        list(range(20)), list(range(33, 0, -1)),
        Random(7).choices(range(-100, 101), k=500),
    ],
)
def test_makeheap(build, values):
    arr = values.copy()
    assert build(arr) is arr
    assert sorted(arr) == sorted(values)
    assert all(arr[(i - 1) // 2] <= arr[i] for i in range(1, len(arr)))
