import pytest

from sort import *


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(
            [4], [4]
        ),
        pytest.param(
            [5, 7, 6, 4], [4, 5, 6, 7]
        ),
    ],
)
def test_bubble_sort(input, expected):
    answer = bubble_sort(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(
            [4], [4]
        ),
        pytest.param(
            [5, 7, 6, 4], [4, 5, 6, 7]
        ),
    ],
)
def test_merge_sort(input, expected):
    answer = merge_sort(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(
            [4], [4]
        ),
        pytest.param(
            [4, 2], [2, 4]
        ),
        pytest.param(
            [5, 7, 6, 4], [4, 5, 6, 7]
        ),
    ],
)
def test_quick_sort(input, expected):
    answer = quick_sort(input)
    assert answer == expected
