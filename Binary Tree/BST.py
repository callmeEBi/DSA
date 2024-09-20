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

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

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
            elif not current_node.right:
                current_node = current_node.left
            elif not current_node.left:
                current_node = current_node.right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    # breadth first search
    def BFS(self):
        queue = []
        results = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    # depth-first traversal
    def dfs_pre_order(self):
        if not self.root:
            return None
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        if not self.root:
            return None
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
print(bst.dfs_pre_order())
