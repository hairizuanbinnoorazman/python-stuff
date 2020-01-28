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


def insert_front(LList, node):
    node.next = LList
    return node
