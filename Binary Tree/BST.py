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

        if not self.root:
            self.root = new_node
            return True
        compared_node = self.root

        while True:

            if value == compared_node.value:
                return False

            if value > compared_node.value:

                if compared_node.right:
                    compared_node = compared_node.right

                else:
                    compared_node.right = new_node
                    return True

            else:

                if compared_node.left:
                    compared_node = compared_node.left

                else:
                    compared_node.left = new_node
                    return True


my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(47)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(52)
my_bst.insert(82)

print(my_bst.root.value)
print(my_bst.root.right.value)
print(my_bst.root.left.value)
print(my_bst.root.right.right.value)
print(my_bst.root.right.left.value)
