# Design a Number Container System

import collections
from unittest.util import sorted_list_difference

class NumberContainers:

    def __init__(self):
        self.boxes = {}
        self.number_lookup = collections.defaultdict(lambda: sorted_list_difference())


    def change(self, index: int, number: int) -> None:
        if index in self.boxes:
            previous = self.boxes[index]
            self.number_lookup[previous].remove(index)
        
        self.boxes[index] = number
        self.number_lookup[number].add(index)

    def find(self, number: int) -> int:
        if len(self.number_lookup[number]) == 0:
                return -1
        return self.number_lookup[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)