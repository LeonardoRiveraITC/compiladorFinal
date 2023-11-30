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

    ?fact: (FLOAT | NUM | CAD | ID )

    ?decl: [TIPODATO] ID ["=" (CAD|ID|[sum]*)] ";"

    ?sum: product
        | sum "+" product   
        | sum "-" product  

    ?product: atom
        | product "*" atom  
        | product "/" atom  

    ?atom: number | ID         

    number: (FLOAT|NUM)
    FLOAT: /(.*)/
    NUM: /(.*)/
 
    CAD: /(.*)/
    TIPODATO: /(.*)/
    ID:/(.*)/

    ?oplog: ">"  
        | EQEQ
        | "<"  
        | ">="
        | "<="  
    
    EQEQ: "=="
    
"""
stable=symbolTableGlobal({})
#modo
mode=state(False)
#stack de errores
errorS=errorStack([])

test=lex('../test/read3.lc',mode,stable,errorS)
test.startLexer()

myParse=parc(grammar,stable,mode,errorS)

myParse.start()

#print(errorS.getErrorStack())
