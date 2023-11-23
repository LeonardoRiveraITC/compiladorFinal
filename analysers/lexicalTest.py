import sys
from os import error
from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
from state import *
import sys
sys.path.append('../utilities/')
from errorStack import *
from lex import *

stable=symbolTableGlobal([])
#modo
mode=state(False)
#stack de errores
errorS=errorStack([])

test=lex('../test/read3.lc',mode,stable,errorS)
test.startLexer()

stable.printTable()
print(errorS.getErrorStack())
