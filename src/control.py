class control:

    def branch(index):
        return index

    def branchNeg(accumulator, index, curr):
        register = accumulator.getAccum()
        if int(register) < 0:
            return index
        else:
            return (curr + 1)

    def branchZero(accumulator, index, curr):
        register = accumulator.getAccum()
        
        if int(register) == 0:
            return index
        else:
            return (curr + 1)

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