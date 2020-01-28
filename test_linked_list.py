import pytest

from linked_list import *


@pytest.mark.parametrize(
    "llist,expected",
    [
        pytest.param(
            Node(4), [4]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7)))), [4, 5, 6, 7]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7, Node(9, Node(11)))))), [
                4, 5, 6, 7, 9, 11]
        ),
    ],
)
def test_linked_list_to_array(llist, expected):
    answer = linked_list_to_array(llist)
    assert answer == expected


@pytest.mark.parametrize(
    "llist,expected",
    [
        pytest.param(
            Node(4), [4]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7)))), [7, 6, 5, 4]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7, Node(9, Node(11)))))), [
                11, 9, 7, 6, 5, 4]
        ),
    ],
)
def test_reverse_linked_list(llist, expected):
    answer = reverse_linked_list(llist)
    answer = linked_list_to_array(answer)
    assert answer == expected


@pytest.mark.parametrize(
    "llist,node,expected",
    [
        pytest.param(
            Node(4), Node(4), [4, 4]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7)))), Node(3), [3, 4, 5, 6, 7]
        ),
        pytest.param(
            Node(4, Node(5, Node(6, Node(7, Node(9, Node(11)))))), Node(71), [
                71, 4, 5, 6, 7, 9, 11]
        ),
    ],
)
def test_insert_front(llist, node, expected):
    answer = insert_front(llist, node)
    answer = linked_list_to_array(answer)
    assert answer == expected
