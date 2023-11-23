class errorStack:
    def __init__(self,error) :
        self.error=error

    def getErrorStack(self):
        return self.error

    def pushErrorStack(self,code,line,info):
        self.error.append(str(code)+" en la linea "+str(line))
    
    def popErrorStack(self):
        self.error.pop()

