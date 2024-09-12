class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        val = new_node.value
        if not self.root:
            self.root = new_node
            return
        compared_node = self.root
        while True:
            if val > compared_node.value:
                if compared_node.right:
                    compared_node = compared_node.right
                else:
                    compared_node.right = new_node
                    return
            if val < compared_node.value:
                if compared_node.left:
                    compared_node = compared_node.left
                else:
                    compared_node.left = new_node
                    return


my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(52)
my_bst.insert(82)

print(my_bst.root.value)  # 47
print(my_bst.root.left.value)  # 21
print(my_bst.root.left.left.value)  # 18
print(my_bst.root.right.value)  # 76
print(my_bst.root.right.right.value)  # 82
print(my_bst.root.right.left.value)  # 52
