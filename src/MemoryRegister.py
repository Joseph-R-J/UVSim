

from array import array
from contextlib import nullcontext


class MemoryRegister:
    
    # initialize the memory register
    def __init__(self):
        self._memoryRegister = ["00000"] * 100
        self.memorySize = 0

    # getter for the memory register
    def getMemoryRegister(self):
        return self._memoryRegister

    # setter for the memory register
    def setMemoryRegister(self, memoryRegister):
        self._memoryRegister = memoryRegister

    # appends the indicated item to the end of the memory register
    def appendToMemoryRegister(self, item):
        if self.memorySize >= 100:
            return "register memory is full"
        else:
            self._memoryRegister[self.memorySize] = item
            self.memorySize += 1

    # inserts requested data into requested index location
    def insertIntoMemoryRegister(self, item, itemIndex):
        self._memoryRegister[itemIndex] = item

    # removes item from memory register by indicated index
    def removeFromMemoryRegister(self, itemIndex):
        if self._memoryRegister[itemIndex]:
            self._memoryRegister[itemIndex] = None
    
    #gets data from requested index location
    def getItemFromMemoryRegister(self, itemIndex):
        if self._memoryRegister[itemIndex]:
            return self._memoryRegister[itemIndex]
        raise Exception("there is no item in this register location")

    def memoryRegisterSize(self):
        return self.memorySize

    def __repr__(self):
        # Quickly retrieves whats in memory for development purposes.
        representation = ""
        for item in self._memoryRegister:
            representation += str(item) + "  "
        return representation