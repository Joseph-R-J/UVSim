
class LoadStoreOperations:

    # Load a word from a specific location in memory into the accumulator.
    def load(MemoryRegisterArray, accumulator, index):
        memoryItem = MemoryRegisterArray.getItemFromMemoryRegister(int(index))
        accumulator.setAccum(memoryItem)
        return None



    # Store a word from the accumulator into a specific location in memory.
    def store(MemoryRegisterArray, accumulator, index):
        accumItem = accumulator.getAccum()
        MemoryRegisterArray.insertIntoMemoryRegister(accumItem, int(index))
        return None
