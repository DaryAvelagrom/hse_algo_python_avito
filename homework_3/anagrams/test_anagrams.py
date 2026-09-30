import pytest

from homework_3.anagrams.algo import group_anagrams


def normalize(groups):
    return sorted(tuple(sorted(group)) for group in groups)


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            [],
            [],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["", ""],
            [["", ""]],
        ),
        (
            ["abc", "bca", "cab"],
            [["abc", "bca", "cab"]],
        ),
        (
            ["abc", "def", "ghi"],
            [["abc"], ["def"], ["ghi"]],
        ),
        (
            ["aaa", "aaa", "aaa"],
            [["aaa", "aaa", "aaa"]],
        ),
        (
            ["ab", "ba", "aab", "aba", "baa"],
            [["ab", "ba"], ["aab", "aba", "baa"]],
        ),
        (
            ["aabb", "baba", "bbaa", "ab", "ba"],
            [["aabb", "baba", "bbaa"], ["ab", "ba"]],
        ),
        (
            ["a", "aa", "aaa", "aaaa"],
            [["a"], ["aa"], ["aaa"], ["aaaa"]],
        ),
        (
            ["az", "za", "zz", "aa"],
            [["az", "za"], ["zz"], ["aa"]],
        ),
        (
            ["listen", "silent", "enlist", "rat", "tar", "art", "abc"],
            [
                ["listen", "silent", "enlist"],
                ["rat", "tar", "art"],
                ["abc"],
            ],
        ),
        (
            ["Eat", "TEA", "ate", "Tan", "NAT", "bat"],
            [["Eat", "TEA", "ate"], ["Tan", "NAT"], ["bat"]],
        ),
    ],
)
def test_group_anagrams(strs, expected):
    assert normalize(group_anagrams(strs)) == normalize(expected)


def test_group_anagrams_does_not_modify_input():
    strs = ["Eat", "tea", "Tan", "ate", "nat", "bat"]
    original = strs.copy()

    group_anagrams(strs)

    assert strs == original
