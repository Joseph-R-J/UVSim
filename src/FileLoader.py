class FileLoader:

    def __init__(self):
        self.fileName = ""
        self.UserInstructions = []
        
    def loadFile(self):
        
        while True:
            try:
                self.fileName = input('If the file is  not in the same directory, please provide the file path. \nPlease enter the file name:')
                file = open(self.fileName, 'r')
                break
                
            except IOError:
                print('Could not find file.')
        
        self.UserInstructions = file.readlines()
        for x in range(len(self.UserInstructions)):
            self.UserInstructions[x] = self.UserInstructions[x].strip()
        file.close()
        return self.UserInstructions
        
     
        
    