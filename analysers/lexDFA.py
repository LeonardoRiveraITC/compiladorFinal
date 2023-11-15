class DFA:
    def __init__(self,Q,Sigma,Delta,q0,F):
        self.Q=Q #estados validos 
        self.Sigma=Sigma #abecedario
        self.Delta=Delta #funciones de transicion 
        self.q0=q0 #estado inicial
        self.F=F #estados de aceptacion

    def getState(self):
        return self.Q

    def start(self,w):
        q=self.q0
        while w!="":
            q=self.Delta[(q,w[0])]
            w=w[1:]
        return q in self.F
