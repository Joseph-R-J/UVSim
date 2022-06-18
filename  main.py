from UvSim import UvSim


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

    while True:
        userInput = input(f"{userCount:02d} ? ")

        if (userInput == "-99999"):
            break

        # Need something to check userInstructions, and also define at what level were dealing with incorrect program input from user.
        userInstructions.append(int(userInput))
        userCount += 1

    program = UvSim(userInstructions)

if __name__ == "__main__":
    main()
