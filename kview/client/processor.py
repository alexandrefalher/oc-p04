from typing import List


class Processor:
    def __init__(self, processes: List[lambda: None]):
        self.processes: List[lambda: None] = processes
        self.position: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.processes) - 1:
            self.position = -1
        self.position += 1
        return self.processes[self.position]
