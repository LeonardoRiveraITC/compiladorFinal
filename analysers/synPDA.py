class  synPDA:
    def __init__(self,states,inputAlf,stackAlf,traslate,start,startStack,stack,accept) :
        self.states=states
        self.inputAlf=inputAlf
        self.stackAlf=stackAlf
        self.start=start 
        self.startStack=startStack
        self.traslate=traslate
        self.accept=accept
        self.stack=stack

    def getInitialState(self):
        return self.start
    def getInitiaStack(self):
        return self.startStack
    
    def changeState(self,actual,w):
        if w in self.inputAlf["constantes"]:
            w=0
        if w in self.inputAlf["operador-logico"]:
            w=1
        if w in self.inputAlf["operador-aritmetico"]:
            w=2
        if w in self.inputAlf["tipo-dato"]:
            w=3
        elif w == "=":
            w=4
        q=(actual,w,self.stack.top)
        if(q in self.states):
            return q 
        else:
            return "DEAD"
        

