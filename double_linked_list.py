class DoubleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def add_last(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove_first(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.remove_first()
            return

        current = self.head
        while current is not None:
            if current.data == data:
                current.prev.next = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return

            current = current.next

    def display(self):
        # forward
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

        # backward
        current = self.tail
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print('None')