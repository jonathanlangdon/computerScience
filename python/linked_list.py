# Use recursive function to search a Linked List for an item


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def linked_list_search(list_node, search_item):
    if list_node.value == search_item:
        return True
    if list_node.next_node == None:
        return False
    return linked_list_search(list_node.next_node, search_item)


node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))  # True
print(linked_list_search(root_node, 3))  # False

root = root = LinkedListNode(
    value=92,
    next_node=LinkedListNode(
        value=9,
        next_node=LinkedListNode(
            value=78,
            next_node=LinkedListNode(
                value=41,
                next_node=LinkedListNode(
                    value=58,
                    next_node=LinkedListNode(
                        value=50, next_node=LinkedListNode(value=42)
                    ),
                ),
            ),
        ),
    ),
)
print(
    linked_list_search(
        root,
        42,
    )
)
