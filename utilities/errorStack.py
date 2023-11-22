class errorStack:
    def __init__(self,error) :
        self.error=error

    def getErrorStack(self):
        return self.error

    def pushErrorStack(self,error,line):
        self.error.append(error+str(line))
    
    def popErrorStack(self):
        self.error.pop()

