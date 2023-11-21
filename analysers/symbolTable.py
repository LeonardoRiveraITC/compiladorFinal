class symbolTableGlobal:
    def __init__(self,table):
        self.table=table

    def getTable(self):
        return self.table

    def addSymbol(self,token,value=''):
        self.table=self.table | {value:token}

    def changeSymbol(self,token,value=''):
        self.table[token]=value

    def deleteSymbol(self,token):
        del (self.table[token])
