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


my_stack = Stack(10)
my_stack.push(20)
my_stack.push(30)
my_stack.print_stack()
print("Height:", my_stack.height)
popped_node = my_stack.pop()
print("Popped:", popped_node.value)
my_stack.print_stack()
print("Height:", my_stack.height)
