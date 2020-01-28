import pytest

from binary_tree import *


@pytest.mark.parametrize(
    "tree,expected",
    [
        pytest.param(
            Node(4), [4]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), [4, 2, 5, 1, 3]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(
                3, Node(8, Node(12)), Node(11))), [4, 2, 5, 1, 12, 8, 3, 11]
        ),
    ],
)
def test_inorder_traversal(tree, expected):
    answer = inorder_traversal(tree)
    assert answer == expected


@pytest.mark.parametrize(
    "tree,expected",
    [
        pytest.param(
            Node(4), [4]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), [1, 2, 4, 5, 3]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(
                3, Node(8, Node(12)), Node(11))), [1, 2, 4, 5, 3, 8, 12, 11]
        ),
    ],
)
def test_preorder_traversal(tree, expected):
    answer = preorder_traversal(tree)
    assert answer == expected


@pytest.mark.parametrize(
    "tree,expected",
    [
        pytest.param(
            Node(4), [4]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), [4, 5, 2, 3, 1]
        ),
    ],
)
def test_postorder_traversal(tree, expected):
    answer = postorder_traversal(tree)
    assert answer == expected


@pytest.mark.parametrize(
    "tree,level,expected",
    [
        pytest.param(
            Node(4), 0, [4]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), 1, [2, 3]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), 2, [4, 5]
        ),
        pytest.param(
            Node(1, Node(2, Node(4), Node(5)), Node(3)), 0, [1]
        ),
    ],
)
def test_levelorder_traversal(tree, level, expected):
    answer = levelorder_traversal(tree, level)
    assert answer == expected


@pytest.mark.parametrize(
    "tree,item,expected",
    [
        pytest.param(
            Node(4), 2, [4, 2]
        ),
        pytest.param(
            None, 2, [2]
        ),
        pytest.param(
            Node(1, Node(-1), Node(3)), 4, [1, -1, 3, 4]
        ),
    ],
)
def test_insert_binary_search_tree(tree, item, expected):
    answer = insert_binary_search_tree(tree, item)
    answer_int = preorder_traversal(answer)
    assert answer_int == expected
