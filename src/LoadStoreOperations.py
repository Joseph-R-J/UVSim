import MemoryRegister

class LoadStoreOperations:

    # Load a word from a specific location in memory into the accumulator.
    def load(MemoryRegisterArray, index):
            return MemoryRegisterArray.getItemFromMemoryRegister(index)
    
    # Store a word from the accumulator into a specific location in memory.
    def store(MemoryRegisterArray, item, index):
        MemoryRegisterArray.insertIntoMemoryRegister(item, index)