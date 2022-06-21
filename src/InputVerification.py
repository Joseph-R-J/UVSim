# verify each user input, should call in main after checking if -99999

def inputVerification(userInput):

    testBool = True # remain true until proven input is not valid

    while testBool == True:

        # test if contains '+' or '-' in userInput[0]
        if userInput[0] != "+" and userInput[0] != "-":
            testBool = False

        # test if input contains 5 characters
        if len(userInput) != 5:
            testBool = False

        # test if last 4 chars are ints
        stringToTest = userInput[1:5]
        if stringToTest.isdigit() != True:
            testBool = False

        return testBool
