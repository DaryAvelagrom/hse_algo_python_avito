import pytest

from palindrome.algo import is_palindrome


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, True),
        (7, True),
        (11, True),
        (121, True),
        (1221, True),
        (12321, True),
        (1223334444333221, True),
        (10, False),
        (100, False),
        (123, False),
        (123421, False),
        (12021, True),
        (6436784365372364782642897482363453467, False),
    ],
)
def test_is_palindrome(number, expected):
    assert is_palindrome(number) == expected
