from os import error
from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
from state import *
import sys
sys.path.append('../utilities/')
from errorStack import *

#alfabeto
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
digito={"0","1","2","3","4","5","6","7","8","9"}
operador={'==','=',"+","-","/","*","<",">"}
operador_logico={'==',"!="}
operador_aritmetico={"+","-","/","*","<",">"}
delimitador={"{","}","(",")",";"}
reservadas={"si":"si","else":"else","mientras":"mientras","entero":"entero","cadena":"cadena","flotante":"flotante","imprimir":"imprimir","teclado":"teclado"}

def Token(estado):
    return {
             1: lambda: "id",
             2: lambda: "num",
             4: lambda: "float",
             5: lambda: "op",
             7: lambda: "cadena",
             8: lambda: "delim" 
            }.get(estado, lambda: None)

def error(estado):
    return {
             3: lambda: 102,
             6: lambda: 101,
             9: lambda: 103 
            }.get(estado, lambda: None)

class lex:
    def __init__(self,file,state,stable,estack):
        self.file=file
        self.stable=stable
        self.state=state
        self.estack=estack



    def startLexer(self):
        #archivo a abrir
        stable=self.stable
        errorS=self.estack
        print(self.file)
        buf=limpiarWhite(self.file)

        automata=DFA({0,1,2,3,4,5,6,7,8,9}, #estados
                     {"alf":alfabeto,"dig":digito,"op":operador,"de":delimitador}, #abecedario
                     {
                         #transiciones 
                         #identificador
                         (0,0):1,
                         (1,0):1,
                         (1,1):1,
                         #entero o flotante
                         (0,1):2,
                         (2,1):2,
                         (2,"."):3,
                         (3,1):4,
                         (4,1):4,
                         #operador
                         (0,2):5,
                         (5,2):5,
                         #cadena
                         (0,'"'):6,
                         (6,0):6,
                         (6,1):6,
                         (6,2):6,
                         (6,3):6,
                         (6,'"'):7,
                         #delimitador
                         (0,3):8,
                         },
                     0, #estado inicial
                     {1,2,4,5,7,8} #estados de aceptacion
                     );

        for el in buf:
            buf1=0
            buf2=buf1
            bufLine=el["buf"]
            bufNum=el["line"]
            while(bufLine[buf2]!='~'):
                buf2=buf1
                state=automata.changeState(automata.getInitial(),bufLine[buf2])
                lastState=state

                while(state!=9):
                    lastState=state
                    buf2+=1
                    state=automata.changeState(state,bufLine[buf2])

                if(lastState not in automata.F):
                    errorS.pushErrorStack(error(lastState)(),str(bufNum))
                    exit()
                    break
                else:
                    t=Token(lastState)()
                    val=bufLine[buf1:buf2]
                    if(val in reservadas):
                        stable.addSymbol("reservada",reservadas[val])
                    elif (val in operador_logico):
                        stable.addSymbol("op_log",val)
                    elif (val in operador_aritmetico):
                        stable.addSymbol("op_ar",val)
                    elif(val == ' '):
                        pass
                    else:
                        stable.addSymbol(t,val)
                    buf1=buf2
        stable.printTable()
