# recursive function to search binary tree


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_search(node, search_value):
    if search_value == node.value:
        return True
    if node.left == None and node.right == None:
        return False
    if search_value > node.value:
        return binary_tree_search(node.right, search_value)
    else:
        return binary_tree_search(node.left, search_value)


root_node = Node(10)
root_node.left = Node(5)
root_node.right = Node(15)
root_node.left.left = Node(3)
root_node.left.right = Node(7)
root_node.right.left = Node(12)
root_node.right.right = Node(18)

print(binary_tree_search(root_node, 18))
print(binary_tree_search(root_node, 7))
print(binary_tree_search(root_node, 15))
print(binary_tree_search(root_node, 10))
print(binary_tree_search(root_node, 1))
print(binary_tree_search(root_node, 11))
print(binary_tree_search(root_node, 21))

# True, True, True, True, False, False, False
