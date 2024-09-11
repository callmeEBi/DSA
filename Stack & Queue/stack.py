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


my_stack = Stack(9)
my_stack.push(83)
my_stack.push(80)
my_stack.push(14)
my_stack.print_stack()


# FIXME - always in a new method:
# consider length
# consider situation with one item in the list
# consider situation with empty list
