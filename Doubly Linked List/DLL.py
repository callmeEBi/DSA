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
        last_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            last_node.prev = None
            last_node.next = None
        elif not self.length:
            return None
        else:
            self.tail = self.tail.prev
            last_node.prev = None
            self.tail.next = None
        self.length -= 1
        return last_node


my_dll = DoublyLinkedList(7)
my_dll.pop()
my_dll.pop()
# my_dll.print_list()

# FIXME - always do this in new method:
# consider length
# consider situation with one item in the list
# consider situation with empty list
