
class LoadStoreOperations:

    # Load a word from a specific location in memory into the accumulator.
    def load(MemoryRegisterArray, accumulator, index):
        memoryItem = MemoryRegisterArray.getItemFromMemoryRegister(index)
        accumulator.setAccum(memoryItem)
        return None


    # Store a word from the accumulator into a specific location in memory.
    def store(MemoryRegisterArray, accumulator, index):
        accumItem = accumulator.getAccum()
        MemoryRegisterArray.insertIntoMemoryRegister(accumItem, index)
        return None
