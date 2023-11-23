class errorStack:
    def __init__(self,error) :
        self.error=error

    def getErrorStack(self):
        return self.error

    def pushErrorStack(self,code,line):
        print(code)
        message=errorMessageSp(code)()
        self.error.append(str(code)+" en la linea "+str(line)+":  "+str(message))
    
    def popErrorStack(self):
        self.error.pop()

    
def errorMessageSp(code):
        return {
         101: lambda: "Cadena mal formada", #cadena incompleta
         102: lambda: "Flotante mal formado", #flotante incompleto
         103: lambda: "Caracter no reconocido" #caracter no reconocido
        }.get(code, lambda: None)
