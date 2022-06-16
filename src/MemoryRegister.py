

from array import array
from contextlib import nullcontext


class MemoryRegister:

    # initialize the memory register
    def __init__(self):
        self._memoryRegister = list()

    # getter for the memory register
    def getMemoryRegister(self):
        return self._memoryRegister

    # setter for the memory register
    def setMemoryRegister(self, memoryRegister):
        self._memoryRegister = memoryRegister

    # appends the indicated item to the end of the memory register
    def appendToMemoryRegister(self, item):
        if len(self._memoryRegister) >= 100:
            return "register memory is full"

        self._memoryRegister.append(item)

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
        return "there is no item in this register location"
