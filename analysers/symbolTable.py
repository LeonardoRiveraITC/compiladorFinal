from pprint import pprint
class symbolTableGlobal:
    def __init__(self,table,id=0):
        self.table=table
        self.id=id

    def getTable(self):
        return self.table

    def addSymbol(self,token,lexema):
        idTable=buscar(self.table,lexema)
        self.id+=1
        if(idTable!=None):
            self.table[self.id]={"reference":idTable,"lex":'',"token":''}
        else:
            self.table[self.id]={"lex":lexema,"token":token,"reference":''}

    def changeSymbol(self,lexema,token=''):
        self.table["token"]=lexema

    def deleteSymbol(self,lexema):
        del (self.table[lexema])

    def printTable(self):
        pprint(self.table)

def buscar(table,lex):
    for i in range(1,len(table)):
        if(table[i]["lex"])==lex:
            return i
    return None

