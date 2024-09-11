class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        self.length += 1


my_queue = Queue(9)
my_queue.enqueue(99)
my_queue.print_queue()

# FIXME - always in a new method:
# consider length
# consider situation with one item in the list
# consider situation with empty list
