from .page_replacement_algorithm import PageReplacementAlgorithm

class FIFOPageReplacement(PageReplacementAlgorithm):
    """
    FIFOPageReplacement is a class that represents the FIFO page replacement algorithm.
    """
    def __init__(self, capacity):
        super().__init__(capacity)
        self.queue = []

    def insert_page(self, page_number):
        if page_number in self.frames:
            pass
        else:
            self.page_faults += 1
            if len(self.frames) < self.capacity:
                self.frames.append(page_number)
                self.queue.append(page_number)
            else:
                oldest_page = self.queue.pop(0)
                self.frames.remove(oldest_page)
                self.frames.append(page_number)
                self.queue.append(page_number)
