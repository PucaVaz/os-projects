class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_node_at_beginning(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def insert_node_at_end(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def delete_any_node(self, node):
        if self.is_empty():
            return

        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        node.next = None
        node.previous = None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()