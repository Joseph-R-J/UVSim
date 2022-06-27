
# Accumulator register class. Single variable for the accumulator, a get and set for that variable

class Accumulator:
    
    def __init__(self, accumVal = 0): # start with zero
        self._accumVal = accumVal

    # getter 
    def getAccum(self):
        return self._accumVal

    # setter 
    def setAccum(self, x):
        self._accumVal = x
        return None
