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

    def shift(self):

        if not self.length:
            return None

        if self.length == 1:
            return self.pop()
        first_node = self.head
        self.head = self.head.next
        self.head.prev = None
        first_node.next = None
        self.length -= 1
        return first_node

    def get(self, index):
        if index >= self.length or index <= 0:
            return
        if index <= self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length, index - 1, -1):
                temp = temp.prev
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
        return True


my_dll = DoublyLinkedList(27)
my_dll.append(46)
my_dll.append(70)
my_dll.append(77)
my_dll.append(15)
my_dll.append(3)

my_dll.set_value(-1, 80)
my_dll.print_list()

# FIXME - always in a new method:
# consider length
# consider situation with one item in the list
# consider situation with empty list
