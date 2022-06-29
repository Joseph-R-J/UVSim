from src.MemoryRegister import MemoryRegister
from src.InputOutputOperations import InputOutputOperations
from src.LoadStoreOperations import LoadStoreOperations
from src.ArithmeticOperations import ArithmeticOperations
from src.control import control
from src.Accumulator import Accumulator
from src.debugger import debugger

class UvSim:
    def __init__(self, commands):
        self.commands = commands
        self.memory = MemoryRegister()
        self.accum = Accumulator()
        self.valid_instructions = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        self.instruct_counter = 0
        self.pos = 0

    def load_program(self):
        for item in self.commands: 
            self.memory.appendToMemoryRegister(item)
        print("*** Program loading completed ***")

    def execute_program(self):

        print("*** Program execution begins  ***")

        regSize = self.memory.memoryRegisterSize()

        while self.pos < regSize:
            instruction = int(self.memory.getItemFromMemoryRegister(self.pos)[1:3])
            number = int((self.memory.getItemFromMemoryRegister(self.pos)[0]) + (self.memory.getItemFromMemoryRegister(self.pos)[3:]))

            # Read
            if instruction == 10:
                self.do_read(number)
            # Write
            elif instruction == 11:
                self.do_write(number)
            # Load
            elif instruction == 20:
                self.do_load(number)
            # Store
            elif instruction == 21:
                self.do_store(number)
            # Add
            elif instruction == 30:
                self.do_add(number)
            # Subtract
            elif instruction == 31:
                self.do_sub(number)
            # Divide
            elif instruction == 32:
                self.do_div(number)
            # Multiply
            elif instruction == 33:
                self.do_mult(number)
            # Branch
            elif instruction == 40:
                self.do_branch(number)
            # Branch neg
            elif instruction == 41:
                self.do_branchneg(number)
            # Branch zero
            elif instruction == 42:
                self.do_branchzero(number)
            # Halt
            elif instruction == 43:
                self.do_halt()

            if instruction in self.valid_instructions:
                self.instruct_counter += 1

            self.pos += 1

        self.simpletron_stats()
        self.memory_stats()
        

    def do_read(self, index):
        InputOutputOperations.read(self.memory, index)

    def do_write(self, index):
        InputOutputOperations.write(self.memory, index)

    def do_load(self, index):
        LoadStoreOperations.load(self.memory, self.accum, index)

    def do_store(self, index):
        print(index)
        LoadStoreOperations.store(self.memory, self.accum, index)

    def do_add(self, index):
        ArithmeticOperations.add(self.memory, self.accum, index)

    def do_sub(self, index):
        ArithmeticOperations.subtract(self.memory, self.accum, index)

    def do_div(self, index):
        ArithmeticOperations.divide(self.memory, self.accum, index)

    def do_mult(self, index):
        ArithmeticOperations.multiply(self.memory, self.accum, index)

    def do_branch(self, pos):
        self.index = control.branch(pos)

    def do_branchneg(self, pos):
        accum_check = control.branchNeg(self.accum)

        if accum_check == True:
            self.index = pos

    def do_branchzero(self, pos):
        accum_check = control.branchZero(self.accum)

        if accum_check == True:
            self.index = pos


    def do_halt(self):
        control.halt()
        self.pos = self.memory.memoryRegisterSize()


    def simpletron_stats(self):
        """Prints simpletron stats to console"""
        item_from_reg = self.memory.getItemFromMemoryRegister(self.instruct_counter-1)
        print(
            "REGISTERS:\n", 
            "Accumulator: ", str(self.accum.getAccum()).rjust(5, '0'), "\n",
            "InstructionCounter: ", str(self.instruct_counter).rjust(5, '0'), "\n",
            "InstructionRegister: ", item_from_reg, "\n",
            "OperationCode: ", int(item_from_reg[1:3]), "\n",
            "Operand: ", str(int((item_from_reg[0]) + (item_from_reg[3:]))).rjust(2, '0'),"\n", sep=""
        )

    def memory_stats(self):
        """Prints out memory to console"""
        debugger.memdump(self.memory.getMemoryRegister())
