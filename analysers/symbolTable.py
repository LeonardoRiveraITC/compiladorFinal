class symbolTable:
    def __init__(self,table):
        self.table=table

    def getTable(self):
        return self.table

    def addSymbol(self,token,value):
        self.table=self.table,{token:value}
