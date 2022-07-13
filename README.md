# UVSim
A simulator for computer science students to learn machine language and computer architecture.

UVSim has a 100 line memory.

Users can input commands one line or multiple lines at a time, which are entered into the memory in sequential order. 

Users can load, save source file from disk.

Users can use the text field to input source file by using insert, delete, cut, paste, etc.

UVSim can handle 6 digit decimal calculations.

OPERATIONS: 

READ = 10 Read a word from the keyboard into a specific location in memory.

WRITE = 11 Write a word from a specific location in memory to screen.

LOAD = 20 Load a word from a specific location in memory into the accumulator.

STORE = 21 Store a word from the accumulator into a specific location in memory.

ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)

SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)

DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).

MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

BRANCH = 40 Branch to a specific location in memory

BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.

BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.

HALT = 43 Pause the program

TERMINATE = -6666

