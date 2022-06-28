class control:

    def branch(index):
        return index

    def branchNeg(accumulator):
        register = accumulator.getAccum()

        if register < 0:
            return True
        else:
            return False

    def branchZero(PC, register, target):
        register = accumulator.getAccum()
        
        if register == 0:
            return True
        else:
            return False

    def halt():
        print("*** Simpletron execution is terminated ***")


#TEST CASE
# i = 0
# x = ["4003", "0", "0", "4106", "0", "0", "4208", "0", "4300", "0", "0", "0"]
# reg1 = -45
# reg2 = 0

# while i != "-9999":

#     op = x[i][:2]
#     target = int(x[i][2:])

#     if op == "40":
#         i = control.branch(i, target)
#     elif op == "41":
#         i = control.branchNeg(i, reg1, target)
#     elif op == "42": 
#         i = control.branchZero(i, reg2, target)
#     elif op == "43":
#         i = control.halt()
#     else: 
#         i += 1

#     print(i)