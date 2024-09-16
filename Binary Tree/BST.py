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

    def __r_insert(self, current_node, value):
        if not current_node:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if not current_node:
            return None
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        else:
            if not current_node.right and not current_node.left:
                return None
            if not current_node.right:
                current_node = current_node.left
            elif not current_node.left:
                current_node = current_node.right
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)


bst = BinarySearchTree()
bst.r_insert(2)
bst.r_insert(1)
bst.r_insert(3)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
