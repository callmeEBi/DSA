class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.length:
            return None
        last_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            last_node.prev = None
            last_node.next = None
        else:
            self.tail = self.tail.prev
            last_node.prev = None
            self.tail.next = None
        self.length -= 1
        return last_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1


my_dll = DoublyLinkedList(27)
my_dll.prepend(95)

my_dll.print_list()

# FIXME - always do this in new method:
# consider length
# consider situation with one item in the list
# consider situation with empty list
