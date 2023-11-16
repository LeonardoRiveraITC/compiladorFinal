from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
buf=limpiarWhite("../test/read.lc")

stable=symbolTableGlobal({})
symbolTable={}
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
digito={"0","1","2","3","4","5","6","7","8","9"}
operador={"=","+","-","/","*"}
delimitador={"{","}","(",")",";"}
reservadas={"si","mientras","entero","cadena","flotante"}

def Token(estado):
    return {
            'b': lambda: "id",
            'c': lambda: "num",
            'e': lambda: "float",
            'f': lambda: "op",
            'h': lambda: "cadena",
            'i': lambda: "delim" 
            }.get(estado, lambda: None)

automata=DFA({"a","b","c","d","e"}, #estados
             {"alf":alfabeto,"dig":digito,"op":operador,"de":delimitador}, #abecedario
             {
                 #transiciones 
                 #identificador
                 ("a","alfabeto"):"b",
                 ("b","alfabeto"):"b",
                 ("b","digito"):"b",
                 #entero o flotante
                 ("a","digito"):"c",
                 ("c","digito"):"c",
                 ("c","."):"d",
                 ("d","digito"):"e",
                 ("e","digito"):"e",
                 #operador
                 ("a","operador"):"f",
                 #cadena
                 ("a",'"'):"g",
                 ("g","alfabeto"):"g",
                 ("g","digito"):"g",
                 ("g",'"'):"h",
                 #delimitador
                 ("a","delimitador"):"i",
                 },
             "a", #estado inicial
             {"b","c","e","f","h","i"} #estados de aceptacion
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
    if(lastState not in automata.F):
        print("error")
        break
    else:
        t=Token(lastState)();
        val=buf[buf1:buf2]
        stable.addSymbol(t,val)
        buf1=buf2
    
print(stable.getTable())
