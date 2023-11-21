class Token:
    def _init_(self, simbolo, tipoToken, linea):
        self.simbolo = simbolo
        self.tipoToken = tipoToken
        self.linea = linea
        self.valor = None
        self.tipoDato = None
        self.alcance = None
        self.operacion = None
        self.expresion = None

    def getExpresion(self):
        return self.expresion

    def setExpresion(self, expresion):
        self.expresion = expresion

    def getSimbolo(self):
        return self.simbolo

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getTipoDato(self):
        return self.tipoDato

    def setTipoDato(self, tipoDato):
        self.tipoDato = tipoDato

    def getTipoToken(self):
        return self.tipoToken

    def getAlcance(self):
        return self.alcance

    def setAlcance(self, alcance):
        self.alcance = alcance

    def getLinea(self):
        return self.linea

    def setLinea(self, linea):
        self.linea = linea

    def getOperacion(self):
        return self.operacion

    def setOperacion(self, operacion):
        self.operacion = operacion