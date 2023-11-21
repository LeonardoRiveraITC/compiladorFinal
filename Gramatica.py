class Gramatica:
    def _init_(self, regex):
        self.patron = re.compile("^" + regex)

    def finalCoincidencias(self, s):
        m = self.patron.match(s)
        if m:
            return m.end()
        return -1

# Definición de los patrones de la gramática
Declaracion_clase = Gramatica("(class)")
Simbolos_especiales = Gramatica("(\\(|\\)|\\{|\\}|\\[|\\]|;)")
Simbolos_de_evaluacion = Gramatica("(<=|>=|<|>|==|!=)")
Asignacion = Gramatica("(=)")
While = Gramatica("(while)")
If = Gramatica("(if)")
Especificador = Gramatica("(boolean|int)")
Booleano_literal = Gramatica("(true|false)")
Modificador = Gramatica("(public|private)")
Operadores_aritmeticos = Gramatica("(\\+|-|/|\\*)")
Operadores_logicos = Gramatica("(&&|\\|\\|)")
Identificador = Gramatica("[a-z]+[1-9]*")
Entero_literal = Gramatica("[1-9]?[0-9]")