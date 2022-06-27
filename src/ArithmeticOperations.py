class ArithmeticOperations:

    # add a word from a specific location in memory
    # to the word in the accumulator (leave result in the accumulator)
    def add(MemoryRegister, Accumulator, index):
        accumVal = Accumulator.getAccum()
        memVal = MemoryRegister.getItemFromMemoryRegister(index)
        accumVal += memval
        Accumulator.setAccum(accumVal)

    # subtract a word from a specific location in 
    # memory from the word in the accumulator (leave the result in accumulator)
    def subtract(MemoryRegister, Accumulator, index):
        accumVal = Accumulator.getAccum()
        memVal = MemoryRegister.getItemFromMemoryRegister(index)
        accumVal -= memval
        Accumulator.setAccum(accumVal)

    # divide the word in the accumulator by a word from a specific location 
    # in memory (leave the result in the accumulator)
    def divide(MemoryRegister, Accumulator, index):
        accumVal = Accumulator.getAccum()
        memVal = MemoryRegister.getItemFromMemoryRegister(index)
        accumVal /= memval
        Accumulator.setAccum(accumVal)

    # multiply a word from a specific location in memory to  
    # the word in the accumulator (leave result in accumulator)
    def multiply(MemoryRegister, Accumulator, index):
        accumVal = Accumulator.getAccum()
        memVal = MemoryRegister.getItemFromMemoryRegister(index)
        accumVal *= memval
        Accumulator.setAccum(accumVal)
