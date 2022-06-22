from src.MemoryRegister import MemoryRegister
from src.InputOutputOperations import InputOutputOperations
from src.LoadStoreOperations import LoadStoreOperations
from src.Accumulator import Accumulator

class UvSim:
    def __init__(self, commands):
        self.commands = commands
        self.memory = MemoryRegister()
        self.accum = Accumulator()

    def load_program(self):
        for item in self.commands: self.memory.appendToMemoryRegister(item)

    def execute_program(self):

        regSize = self.memory.memoryRegisterSize()

        for index in range(0, regSize + 1):
            instruction = str(self.memory.getItemFromMemoryRegister(index))[:2]
            number = str(self.memory.getItemFromMemoryRegister(index))[2:]

            # Read
            if instruction == '10':
                self.do_read(number)
            # Write
            elif instruction == '11':
                self.do_write(number)
            # Load
            elif instruction == '20':
                self.do_load(number)
            # Store
            elif instruction == '21':
                self.do_store(number)
            # Add
            elif instruction == '30':
                self.do_add()
            # Subtract
            elif instruction == '31':
                self.do_sub()
            # Divide
            elif instruction == '32':
                self.do_div()
            # Multiply
            elif instruction == '33':
                self.do_mult()
            # Branch
            elif instruction == '40':
                self.do_branch()
            # Branch neg
            elif instruction == '41':
                self.do_branchneg()
            # Branch zero
            elif instruction == '42':
                self.do_branchzero()
            # Halt
            elif instruction == '43':
                self.do_halt()
    
        print(self.memory)


    def do_read(self, index):
        InputOutputOperations.read(self.memory, index)
    def do_write(self, index):
        InputOutputOperations.write(self.memory, index)
    def do_load(self, index):
        LoadStoreOperations.load(self.memory, self.accum, index)
    def do_store(self):
        pass
    def do_add(self):
        pass
    def do_sub(self):
        pass
    def do_div(self):
        pass
    def do_mult(self):
        pass
    def do_branch(self):
        pass
    def do_branchneg(self):
        pass
    def do_branchzero(self):
        pass
    def do_halt(self):
        pass
