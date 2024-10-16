from .page_replacement_algorithm import PageReplacementAlgorithm
from ..data_structures.doubly_linked_list import DoublyLinkedList
from ..data_structures.node import Node


class LeastUsedPageReplacement(PageReplacementAlgorithm):
    """
    Least Recently Used (LRU) page replacement algorithm.
    """
    def __init__(self, capacity):
        super().__init__(capacity)
        self.memory = DoublyLinkedList()
        self.page_map = {}
        self.size = 0

    def insert_page(self, page_number):
        if page_number in self.page_map:
            node = self.page_map[page_number]
            self.memory.move_node_to_end(node)
        else:
            self.page_faults += 1
            if self.size < self.capacity:
                self.size += 1
            else:
                self.replace_page()

            new_node = Node(page_number)
            self.page_map[page_number] = new_node
            self.memory.insert_node_at_end(new_node)

    def replace_page(self):
        node_to_remove = self.memory.head
        del self.page_map[node_to_remove.data]
        self.memory.delete_any_node(node_to_remove)