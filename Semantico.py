class Semantico:
    def _init_(self, listaTokens):
        self.tabla = {}
        self.listaTokens = listaTokens
        self.errores = ""
        self.indice = 0
        self.bloque = 0

    def comenzarAnalisis(self):
        for t in self.listaTokens:
            if t.getSimbolo() == "{":
                self.bloque += 1
            elif t.getSimbolo() == "}":
                self.bloque -= 1
            if t.getOperacion() is not None:
                if t.getTipoToken() == Gramatica.Identificador and not t.getOperacion() == "clase":
                    if t.getOperacion() == "declaracion":
                        self.insertarDeclaracion(t)
                    elif t.getOperacion() == "asignacion" or t.getOperacion() == "expresion":
                        self.validarOperacion(t)
                    self.validarTipodeDatos(t)
            self.indice += 1
        return self.errores == ""

    def validarOperacion(self, t):
        if not self.validarDeclaracion(t):
            return
        aux = self.tabla.get(t.getSimbolo())
        operador = self.listaTokens[self.indice + 1].getTipoToken()
        if aux.getTipoDato() == "Entero" and (operador != Gramatica.Simbolos_de_evaluacion and operador != Gramatica.Asignacion):
            self.errores += "Se usaron operadores incorrectos para la variable " + t.getSimbolo() + " en la línea: " + str(t.getLinea()) + "\n"
        elif aux.getTipoDato() == "Booleano" and operador != Gramatica.Operadores_logicos and operador != Gramatica.Asignacion:
            self.errores += "Se usaron operadores incorrectos para la variable " + t.getSimbolo() + " en la línea: " + str(t.getLinea()) + "\n"

    def validarTipodeDatos(self, t):
        if t.getOperacion() == "expresion":
            return
        if not self.validarDeclaracion(t):
            return
        aux = self.tabla.get(t.getSimbolo())
        tipo = self.getTipoDato(t.getValor())
        if aux.getTipoDato() == "Entero" and tipo != Gramatica.Entero_literal:
            self.errores += "La variable " + t.getSimbolo() + " es de tipo entero y recibe el valor \"" + t.getValor() + "\" en la línea: " + str(t.getLinea()) + "\n"
        elif aux.getTipoDato() == "Booleano" and tipo != Gramatica.Booleano_literal:
            self.errores += "La variable " + t.getSimbolo() + " es de tipo booleano y recibe el valor \"" + t.getValor() + "\" en la línea: " + str(t.getLinea()) + "\n"

    def validarDeclaracion(self, t):
        if t.getSimbolo() not in self.tabla:
            self.errores += "La variable \"" + t.getSimbolo() + "\" no se encuentra declarada. Fue usada en la línea: " + str(t.getLinea()) + "\n"
            return False
        return True

    def insertarDeclaracion(self, t):
        if t.getSimbolo() not in self.tabla:
            t.setAlcance("B" + str(self.bloque))
            self.tabla[t.getSimbolo()] = t
        else:
            self.errores += "La variable " + t.getSimbolo() + " ya se encuentra declarada en la línea " + str(self.tabla[t.getSimbolo()].getLinea()) + " y se declaró de nuevo en la línea " + str(t.getLinea()) + "\n"

    def getTipoDato(self, entrada):
        for t in Gramatica:
            fin = t.finalCoincidencias(entrada)
            if fin != -1:
                return t
        return None

    def getTabla(self):
        return self.tabla

    def getErrores(self):
        return self.errores