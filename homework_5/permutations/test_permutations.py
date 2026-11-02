from itertools import permutations as reference_permutations
from math import factorial

import pytest

from homework_5.permutations.algo import permutations


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                     [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([], [[]]),
        ([-1, 0], [[-1, 0], [0, -1]]),
    ],
)
def test_examples(nums, expected):
    assert permutations(nums) == expected


@pytest.mark.parametrize("size", range(7))
def test_all_permutations(size):
    nums = list(range(size))
    original = nums.copy()
    result = permutations(nums)
    assert result == [list(item) for item in reference_permutations(nums)]
    assert len(result) == factorial(size)
    assert nums == original
    assert len({id(item) for item in result}) == len(result)


def test_repeated_values():
    assert permutations([1, 1, 2]) == [
        [1, 1, 2], [1, 2, 1], [1, 1, 2],
        [1, 2, 1], [2, 1, 1], [2, 1, 1],
    ]


def test_visualization(capsys):
    permutations([0, 1])
    assert capsys.readouterr().out.splitlines() == [
        "-> backtrack([])",
        "  -> backtrack([0])",
        "    -> backtrack([0, 1])",
        "    <- backtrack = None",
        "  <- backtrack = None",
        "  -> backtrack([1])",
        "    -> backtrack([1, 0])",
        "    <- backtrack = None",
        "  <- backtrack = None",
        "<- backtrack = None",
    ]


def test_independent_calls_and_results():
    first = permutations([1, 2])
    first[0].append(3)
    assert first[1] == [2, 1]
    assert permutations([1, 2]) == [[1, 2], [2, 1]]
