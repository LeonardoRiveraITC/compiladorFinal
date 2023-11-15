from scan import limpiarWhite
from lexDFA import * 
buf=limpiarWhite("../test/read.lc")

tBuf1=0;
tBuf2=0;
counter=0
symbolTable={}
estado='a'
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
digito={"0","1","2","3","4","5","6","7","8","9"}
operador={"=","+","-","/","*"}
delimitador={'"',"(",")"}
reservadas={"si","mientras","entero","cadena","flotante"}

automata=DFA({"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p"}, #estados
             [alfabeto,digito,operador,delimitador], #abecedario
             {
                 #transiciones 
                 #identificador
                 ("a","alfabeto"):"b",
                 ("b","alfabetodigito"):"b",
                 #entero o flotante
                 ("a","digito"):"c",
                 ("c","digito"):"c",
                 ("c","."):"d",
                 ("d","digito"):"e",
                 ("e","digito"):"e",
                 #keywords
                 #si
                 ("a","s"):"f",
                 ("f","i"):"g",
                 ("g",""):"h",
                 #if-identificador
                 ("f","alfabetodigito"):"b",
                 ("g","alfabetodigito"):"b",
                 #while 
                 #("a","w"):"i",
                 #("i","h"):"j",
                 #("j","i"):"k",
                 #("k","l"):"l",
                 #("l","e"):"m",
                 #("m",""):"n",
                 #while-identificador
                 #("i","alfabetodigito"):"b",
                 #("j","alfabetodigito"):"b",
                 #("k","alfabetodigito"):"b",
                 #("l","alfabetodigito"):"b",
                 #("m","alfabetodigito"):"b",
                 #cadena
                 #("o",'"'):"p",
                 #("p","alfabetodigito"):"q",
                 #("q",'"'):"r",
                 },
             "a", #estado inicial
             {"b","c","e","h","p"} #estados de aceptacion
             );




print (buf)
