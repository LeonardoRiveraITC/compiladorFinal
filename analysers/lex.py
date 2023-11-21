from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
from state import *

buf=limpiarWhite("../test/read.lc")

stable=symbolTableGlobal({})
symbolTable={}
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
digito={"0","1","2","3","4","5","6","7","8","9"}
operador={"=","+","-","/","*"}
delimitador={"{","}","(",")",";"}
reservadas={"si","mientras","entero","cadena","flotante"}

mode=state(False)

def Token(estado):
    return {
             1: lambda: "id",
             2: lambda: "num",
             4: lambda: "float",
             5: lambda: "op",
             6: lambda: "cadena",
             8: lambda: "delim" 
            }.get(estado, lambda: None)

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
                 #cadena
                 (0,'"'):6,
                 (6,0):6,
                 (6,1):6,
                 (6,'"'):7,
                 #delimitador
                 (0,3):8,
                 },
             0, #estado inicial
             {1,2,4,5,7,8} #estados de aceptacion
             );
buf1=0
while(buf1<len(buf) and buf[buf1]!=' '):
    buf2=buf1
    state=automata.changeState(automata.getInitial(),buf[buf1])
    lastState=state
    while (state!=False):
        buf2=buf2+1
        lastState=state
        state=automata.changeState(state,buf[buf2])
        mode.step('Estado actual: '+  str(lastState) + ' | Caracter leido:' + buf[buf2])
    if(lastState not in automata.F):
        print("error")
        break
    else:
        print(lastState)
        t=Token(lastState)();
        val=buf[buf1:buf2]
        stable.addSymbol(t,val)
        buf1=buf2
    
print(stable.getTable())
