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
            elif value > comparing.value:
                comparing = comparing.right
            else:
                comparing = comparing.left
        return False

    def __r_contains(self, current_node, value):
        if not current_node:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)

print(bst.r_contains(5))

# print(bst.insert(15))  # True
# print(bst.insert(10))  # False
# print(bst.contains(10))  # True
# print(bst.contains(5))  # True
# print(bst.contains(15))  # True
# print(bst.contains(20))  # False
