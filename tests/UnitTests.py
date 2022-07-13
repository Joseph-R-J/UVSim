from UvSim import UvSim


class UnitTests:

    memoryRegister = memoryRegister()
    accumulator = Accumulator()

    def testArithmeticOperations():
        arithemtic = ArithmeticOperations()
        self.memoryRegister.insertIntoMemoryRegister(10, 0)
        self.accumulator.setAccum(50)
        arithemtic.add(self.memoryRegister, self.accumulator, 0)
        value = self.accumulator.getAccum()
        assert value == 60, f"addition yielded an incorrect result. Expected 60, got {value}"
        arithemtic.subtract(self.memoryRegister, self.accumulator, 0)
        value = self.accumulator.getAccum()
        assert value == 40, f"subtraction yielded an incorrect result. Expected 40, got {value}"
        arithemtic.divide(self.memoryRegister, self.accumulator, 0)
        value = self.accumulator.getAccum()
        assert value == 5, f"division yielded an incorrect result. Expected 5, got {value}"
        arithemtic.multiply(self.memoryRegister, self.accumulator, 0 )
        value = self.accumulator.getAccum()
        assert value == 500, f"multiplicaton yielded an incorrect result. Expected 500, got {value}"

    def testLoadStoreOperations():
        loadStore = LoadStoreOperations()
        self.memoryRegister.insertIntoMemoryRegister(20, 0)
        loadStore.load(self.memoryRegister, self.accumulator, 0)
        value = self.accumulator.getAccum()
        assert value == 20, f"load yielded an incorrect result. Expected 20, got {value}"
        loadStore.store(self.memoryRegister, self.accumulator, 1)
        value = self.memoryRegister.getItemFromMemoryRegister(1)
        assert value == 20, f"store yielded an incorrect result. Expected 20, got {value}"

