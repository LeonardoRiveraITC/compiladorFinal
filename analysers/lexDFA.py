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
        if w in self.Sigma["alf"]: #alfabeto
            w=0
        elif w in self.Sigma["dig"]: #digito
            w=1
        elif w in self.Sigma["op"]: #operador
            w=2
        elif w in self.Sigma["de"]: #delimitador
            w=3
        q=(state,w)
        if q in self.Delta:
            return self.Delta[q]
        else:
            return False 
