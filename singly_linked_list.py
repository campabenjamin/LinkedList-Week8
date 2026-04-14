class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None
    
    def add_first(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self.size += 1

    def add_last(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1

            if self.head is None:
                self.tail = None
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return    
            current = current.next

    def remove_first(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')