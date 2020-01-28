class Node:
    def __init__(self, item, next=None):
        self.value = item
        self.next = next


def linked_list_to_array(LList):
    item = []
    if LList is None:
        return []
    item = item + [LList.value]
    zz = LList
    while zz.next is not None:
        item = item + [zz.next.value]
        zz = zz.next
    return item


def reverse_linked_list(LList):
    if LList.next is None:
        return LList
    prev_node = None
    current_node = LList

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        if next_node is None:
            return current_node
        else:
            current_node = next_node


def insert_front(LList, node):
    node.next = LList
    return node
