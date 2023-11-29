import sys
from os import error
from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
from state import *
from parser import *
import sys
sys.path.append('../utilities/')
from errorStack import *
from lex import *
grammar = """
    ?start: block 

    ?block: "{" ([decision] [iteracion] [decl])* "}"  

    ?decision: "si" "(" exprlog ")" block 

    ?iteracion: "mientras" "(" exprlog ")" block 

    ?exprlog: fact 
            | fact oplog fact

    ?fact: (number | cadena | id)

    ?decl: [tipodato] id ["=" (cadena|id|[sum]*)] ";"

    ?sum: product
        | sum "+" product   
        | sum "-" product  

    ?product: atom
        | product "*" atom  
        | product "/" atom  

    ?atom: number | id         

    number: ("float"|"num")
    cadena: "cad"
    tipodato: ("cadena"| "flotante" | "entero")
    id:"id"

    oplog: ">"  
        | "<"  
        | ">="
        | "<="  
        | "==" 

"""
stable=symbolTableGlobal({})
#modo
mode=state(False)
#stack de errores
errorS=errorStack([])

test=lex('../test/read3.lc',mode,stable,errorS)
test.startLexer()

myParse=parc(grammar,stable,mode)

myParse.start()

print(errorS.getErrorStack())
