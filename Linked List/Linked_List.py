class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.tail = new_node
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        popped_value = self.tail
        if self.head is None:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return popped_value

    def prepend(self, value):
        new_node = Node(value=value, next=self.head)
        self.head = new_node
        if not self.length:
            self.tail = new_node
        self.length += 1
        return True

    def shift(self):
        if not self.head:
            return
        if self.length == 1:
            self.tail == None
        shifted_value = self.head
        self.head = self.head.next
        shifted_value.next = None
        self.length -= 1

        return shifted_value

    def get(self, index):
        if index >= self.length or index < 0:
            return
        result = self.head
        for _ in range(index):
            result = result.next
        return result

    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        else:
            current_node = Node(value)
            before_node = self.get(index - 1)
            current_node.next = before_node.next
            before_node.next = current_node
            self.length += 1
            return True

    def remove(self, index):
        before_node = self.get(index - 1)
        current_node = self.get(index)
        after_node = self.get(index + 1)
        before_node.next = after_node
        current_node.next = None
        current_node.value = None


my_linked_list = LinkedList(4)
my_linked_list.append_end(3)
my_linked_list.append_end(7)
my_linked_list.append_end(2)
my_linked_list.append_end(8)

my_linked_list.remove(2)

my_linked_list.print_list()
