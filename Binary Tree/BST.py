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

    def contains(self, value):
        comparing = self.root
        while comparing:
            if value == comparing.value:
                return True
            if value > comparing.value:
                comparing = comparing.right
            else:
                comparing = comparing.left
        return False


my_bst = BinarySearchTree()
my_bst.insert(67)
my_bst.insert(97)
my_bst.insert(11)
my_bst.insert(17)
my_bst.insert(63)
my_bst.insert(75)
my_bst.insert(67)
my_bst.insert(30)
my_bst.insert(22)
my_bst.insert(15)

print(my_bst.contains(888))
