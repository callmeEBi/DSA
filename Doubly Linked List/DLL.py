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
        if index >= self.length or index < 0:
            print("here")
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

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        after = self.get(index)
        before = after.prev
        after.prev = new_node
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        self.length += 1

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        current_node = self.get(index)
        before = current_node.prev
        after = current_node.next
        before.next = after
        after.prev = before
        current_node.next = None
        current_node.prev = None
        self.length -= 1
        return current_node



my_dll = DoublyLinkedList(27)
print("Initial List:")
my_dll.print_list()

print("\nAppend 28:")
my_dll.append(28)
my_dll.print_list()

print("\nPrepend 26:")
my_dll.prepend(26)
my_dll.print_list()

print("\nPop:")
popped_node = my_dll.pop()
print("Popped Node:", popped_node.value)
my_dll.print_list()

print("\nShift:")
shifted_node = my_dll.shift()
print("Shifted Node:", shifted_node.value)
my_dll.print_list()

print("my print:")
my_dll.print_list()
print("\nGet 0:")
node = my_dll.get(0)
print("Node at Index 0:", node.value)

print("\nSet Value at Index 1 to 29:")
my_dll.set_value(1, 29)
my_dll.print_list()

print("\nInsert 30 at Index 1:")
my_dll.insert(1, 30)
my_dll.print_list()

print("\nRemove Node at Index 1:")
removed_node = my_dll.remove(1)
print("Removed Node:", removed_node.value)
my_dll.print_list()
