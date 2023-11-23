from pprint import pprint
class symbolTableGlobal:
    def __init__(self,table):
        self.table=table

    def getTable(self):
        return self.table

    def addSymbol(self,lexema='',token=''):
        self.table=self.table | {token:lexema}

    def changeSymbol(self,lexema,token=''):
        self.table[token]=lexema

    def deleteSymbol(self,lexema):
        del (self.table[lexema])
    
    def printTable(self):
        print("lexema   |   token") 
        pprint(self.table)
