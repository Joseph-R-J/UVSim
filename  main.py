from re import L
from UvSim import UvSim
from FileLoader import LoadFile


def main():

    # User Instructions
    print("*** Welcome to UVSim! ***",
    "*** Please enter your program one instruction ***",
    "*** ( or data word ) at a time into the input ***",
    "*** text field. I will display the location   ***",
    "*** number and question mark (?). You then    ***",
    "*** type the word for that location. Enter    ***",
    "*** -99999 to stop entering your program.     ***",
    sep='\n', end='\n')

    userCount = 0
    userInstructions = list()

    method = input("\nFor line by line, enter 1. For all at once, comma delimited, enter 2. To load a file, enter 3: ")
    if method == "1":
        while True:
            userInput = input(f"{userCount:02d} ? ")

            if (userInput == "-99999"):
                break

            # Need something to check userInstructions, and also define at what level were dealing with incorrect program input from user.
            userInstructions.append(userInput)
            userCount += 1
    elif method == "2":
        commands = input("Enter your commands here, comma delimited:\n\n")
        userInstructions = commands.split(",")
        for x in range(len(userInstructions)):
            userInstructions[x] = userInstructions[x].strip()
    elif method =='3':
        userInstuctions = fileLoader.LoadFile()

    program = UvSim(userInstructions)
    program.load_program()
    program.execute_program()

if __name__ == "__main__":
    main()