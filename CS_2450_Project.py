"""
CS-2450 Term Project
Jacob Thornhill
"""

class uvsim:
    memSize = 100
    memory = [None] * memSize # fill each register with 'None'
    accumulator = -1
    pc = 0
    operand = 0
    opcode = 0
    count = 0
    instructCount = 0

    # input, output operations
    def read(op): 
        uvsim.memory.insert(op, input("Enter an Integer: "))
    def write(op): 
        print("Contents of " + str(op) + "is " + str(uvsim.memory[op]))

    # load, store operations
    def load(op): 
        uvsim.accumulator = int(uvsim.memory[op])
    def store(op): 
        uvsim.memory[op] = str(uvsim.accumulator)

    # arithmetic operations
    def add(op): 
        uvsim.accumulator += int(uvsim.memory[op])
    def subtract(op): 
        uvsim.accumulator -= int(uvsim.memory[op])
    def divide(op): 
        uvsim.accumulator /= int(uvsim.memory[op])
    def multiply(op): 
        uvsim.accumulator *= int(uvsim.memory[op])

    # control operations
    def branch(op): 
        uvsim.pc = op - 1
    def branchNeg(op): 
        if uvsim.accumulator < 0: 
            uvsim.pc = op - 1
    def branchZero(op): 
        if uvsim.accumulator == 0:
            uvsim.pc = op - 1
    def halt(op): 
        uvsim.pc = 101

    # function to select right operation to use on operand
    def runProgram():
    
        print("*** Program execution begins ***")

        while(uvsim.pc < uvsim.memSize):
            
            if uvsim.memory[uvsim.pc] != None:
                
                uvsim.opcode = int(uvsim.memory[uvsim.pc][:2]) # opcode is first 2 digits
                uvsim.operand = int(uvsim.memory[uvsim.pc][2:]) # operand remaining digits
    
                if uvsim.opcode == 10: 
                    uvsim.read(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 11:
                    uvsim.write(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 20:
                    uvsim.load(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 21:
                    uvsim.store(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 30:
                    uvsim.add(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 31:
                    uvsim.subtract(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 32:
                    uvsim.divide(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 33:
                    uvsim.multiply(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 40:
                    uvsim.branch(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 41:
                    uvsim.branchNeg(uvsim.operand)
                    uvsim.instructCount += 1
                elif uvsim.opcode == 43:
                    uvsim.halt(uvsim.operand)
                    uvsim.instructCount += 1
                else: 
                    print("opcode not found")

                uvsim.pc += 1 # increment program counter after each pass
            
            else:   # exit, current memory cell is 'None'
                return

    def displayInstructions():
        # intro text:
        print("*** Welcome to UVSim! ***")
        print("*** Please enter your program one instruction ***")
        print("*** ( or data word ) at a time into the input ***")
        print("*** text field. I will display the location ***")
        print("*** number and question mark (?). You then ***")
        print("*** type the word for that location. Enter ***")
        print("*** -99999 to stop entering your program. ***")

    def GetUserInput():
        
        while(True): # run til break
            updateString = '{:0>2}'.format(uvsim.count) + " ? "
            userInput = input(updateString)

            if userInput == "-99999": # end
                break
            
            if len(userInput) == 5: # valid argument, must be 5 chars
                
                if userInput[0] == "+" or userInput[0] == "-":
                    uvsim.memory.insert(uvsim.count, userInput[1:5]) # take away '-' or '+'
                    uvsim.count += 1

                else:
                    print("Invalid instruction given, missing + or - sign")

            else:
                print("Invalid instruction given, try again.")

        print("*** Program loading completed ***")

    def showStats():
        instructReg = str(uvsim.opcode) + str('{:0>2}'.format(uvsim.operand))
        print("*** Simpletron execution terminated ***")
        print("REGISTERS:")
        print("Accumulator:             " + '{:0>5}'.format(uvsim.accumulator))
        print("Instructioncounter:      " + '{:0>2}'.format(uvsim.instructCount))
        print("InstructionRegister:     " + '{:0>5}'.format(instructReg))
        print("OperationCode:           " + str(uvsim.opcode))
        print("Operand:                 " + '{:0>2}'.format(uvsim.operand))

        # just need to print memory registers here

# main driver
def main():
    uvsim.displayInstructions()
    uvsim.GetUserInput()
    uvsim.runProgram()
    uvsim.showStats()

if __name__ == "__main__":
    main()



