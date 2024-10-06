from .page_replacement_algorithm import PageReplacementAlgorithm
from ..data_structures.doubly_linked_list import DoublyLinkedList
from ..data_structures.node import Node

class OptimalPageReplacement(PageReplacementAlgorithm):
    def __init__(self, capacity, page_references):
        super().__init__(capacity)
        self.page_references = page_references
        self.page_map = {}
        self.memory = DoublyLinkedList()
        self.size = 0
        self.current_index = 0

    def insert_page(self, page_number):
        if page_number in self.page_map:
            pass
        else:
            self.page_faults += 1
            if self.size >= self.capacity:
                self.replace_page()
            else:
                self.size += 1

            new_node = Node(page_number)
            self.page_map[page_number] = new_node
            self.memory.insert_node_at_end(new_node)

        self.current_index += 1

    def replace_page(self):
        node_to_remove = self.find_page_to_replace()
        self.memory.delete_any_node(node_to_remove)
        del self.page_map[node_to_remove.data]
        self.size -= 1

    def find_page_to_replace(self):
        farthest_future_use = -1
        node_to_remove = None

        current_node = self.memory.head
        while current_node:
            page_number = current_node.data
            try:
                next_use = self.page_references.index(page_number, self.current_index)
            except ValueError:
                next_use = float('inf')

            if next_use > farthest_future_use:
                farthest_future_use = next_use
                node_to_remove = current_node

            current_node = current_node.next

        return node_to_remove

    def print_memory_state(self):
        current = self.memory.head
        pages_in_memory = []
        while current:
            pages_in_memory.append(current.data)
            current = current.next
        print(f"Frames: {pages_in_memory}")
