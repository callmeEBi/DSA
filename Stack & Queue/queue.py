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
        if self.length == 0:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        first_node = self.first
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        first_node.next = None
        self.length -= 1
        return first_node


queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", end=" ")
queue.print_queue()
print("\nDequeued:", queue.dequeue().value)
print("Queue:", end=" ")
queue.print_queue()
print("\nDequeued:", queue.dequeue().value)
print("Queue:", end=" ")
queue.print_queue()
print("\nDequeued:", queue.dequeue().value)
print("Queue:", end=" ")
queue.print_queue()
print("\nDequeued:", queue.dequeue())
