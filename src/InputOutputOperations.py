class InputOutputOperations:

    # Read a word from the keyboard into a specific location in memory.
    def read(MemoryRegisterArray, index):
        word = input("Enter an integer: ")
        MemoryRegisterArray.insertIntoMemoryRegister(word, int(index))
        return None

    
    # Write a word from a specific location in Memory to screen.
    def write(MemoryRegisterArray, index):
        print(f"Contents of {index} is {MemoryRegisterArray.getItemFromMemoryRegister(int(index))}")
        return None
