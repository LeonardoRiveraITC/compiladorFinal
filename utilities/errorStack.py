class errorStack:
    def __init__(self,error) :
        self.error=error

    def getErrorStack(self):
        return self.error

    def cleanErrorStack(self):
        self.error=[]

    def pushErrorStack(self,code,line):
        message=errorMessageSp(code)()
        self.error.append(str(code)+" en la linea "+str(line)+":  "+str(message))
        print(self.error)
    
    def popErrorStack(self):
        self.error.pop()

    
def errorMessageSp(code):
        return {
         101: lambda: "Cadena mal formada", #cadena incompleta
         102: lambda: "Flotante mal formado", #flotante incompleto
         103: lambda: "Caracter no reconocido", #caracter no reconocido
         200: lambda: "Regla mal formada:", #caracter no reconocido
         301: lambda: "Asignación a un identificador no declarado" ,
         302: lambda: "Intento de asignacion de una cadena a un numerico" ,
         303: lambda: "Intento de asignacion de numerico en cadena", 
         304: lambda: "Intento de operacion logica con una variable no existente", 
         305: lambda: "Intento de operacion logica con una cadena", 
        }.get(code, lambda: None)
