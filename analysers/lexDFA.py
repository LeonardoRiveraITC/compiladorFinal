class DFA:
    def __init__(self,Q,Sigma,Delta,q0,F):
        self.Q=Q #estados validos 
        self.Sigma=Sigma #abecedario
        self.Delta=Delta #funciones de transicion 
        self.q0=q0 #estado inicial
        self.F=F #estados de aceptacion

    def getState(self):
        return self.Q

    def getInitial(self):
        return self.q0

    def changeState(self,state,w):
        if w in self.Sigma["alf"]:
            w="alfabeto"
        elif w in self.Sigma["dig"]:
            w="digito"
        elif w in self.Sigma["op"]:
            w="operador"
        elif w in self.Sigma["de"]:
            w="delimitador"
        q=(state,w)
        if q in self.Delta:
            return self.Delta[q]
        else:
            return False 
