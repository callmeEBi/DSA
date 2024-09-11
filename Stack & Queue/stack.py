class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        last_node = self.top
        self.top = self.top.next
        last_node.next = None
        self.height -= 1
        return last_node


my_stack = Stack(9)
my_stack.pop()
my_stack.push(88)
my_stack.print_stack()


# FIXME - always in a new method:
# consider height
# consider situation with one item in the list
# consider situation with empty list
