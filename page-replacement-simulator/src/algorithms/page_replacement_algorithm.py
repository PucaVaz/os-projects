class PageReplacementAlgorithm:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_faults = 0
        self.frames = [] 

    def insert_page(self, page_number):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_page_faults(self):
        return self.page_faults

    def print_memory_state(self):
        print(f"Frames: {self.frames}")