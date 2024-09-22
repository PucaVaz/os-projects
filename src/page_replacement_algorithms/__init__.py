class PageReplacementSimulator:
    def __init__(self, memory_simulation_data):
        self.frame_count = memory_simulation_data['frames']
        self.page_references = memory_simulation_data['processes']

    def fifo(self):
        page_faults = 0
        frames = []
        for page in self.page_references:
            if page not in frames:
                if len(frames) < self.frame_count:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
                page_faults += 1
        return page_faults
    
    def optimal(self):
        page_faults = 0
        frames = []
        for page in self.page_references:
            if page not in frames:
                if len(frames) < self.frame_count:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
                page_faults += 1
        return page_faults
    
    def lru(self):
        page_faults = 0
        frames = []
        for page in self.page_references:
            if page not in frames:
                if len(frames) < self.frame_count:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
                page_faults += 1
        return page_faults
    
