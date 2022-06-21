# do I need these 3 imports?

    #import LoadStoreOperations
    #import InputOutputOperations
    #import ArithmeticOperations

import MemoryRegister

# function to select right operation to use on operand
def executeProgram(MemoryRegisterArray):

    regArrLen = len(MemoryRegisterArray) # number of used memory cells
    pc = 0 # program counter

    while (pc < regArrLen):

        word = getItemFromMemoryRegister(pc) # get next word

        opcode = word[:2] # opcode is first 2 digits
        operand = word[2:] # operand remaining digits

        # find right function and call with operand
        if opcode == 10: 
            read(operand)
        elif opcode == 11:
            write(operand)
        elif opcode == 20:
            load(operand)
        elif opcode == 21:
            store(operand)
        elif opcode == 30:
            add(operand)
        elif opcode == 31:
            subtract(operand)
        elif opcode == 32:
            divide(operand)
        elif opcode == 33:
            multiply(operand)
        elif opcode == 40:
            branch(operand)
        elif opcode == 41:
            branchNeg(operand)
        elif opcode == 43:
            halt(operand)
        else: 
            print("opcode not found")

        pc += 1 # increment program counter 

    return


