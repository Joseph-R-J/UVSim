class FileLoader

    def __init__(self):
        self.fileName = ""
        self.UserInstructions = []
        
    def LoadFile(self):
        
        while true
            try:
                self.fileName = input('If the file is  not in the same directory, please provide the file path. \n Please enter the file name:')
                file = open(fileName, r)
                break
                
            except IOError:
                print('Could not find file.')
        
        self.UserInstructions = file.readlines()
         
        return self.UserInstructions
        
     
        
    