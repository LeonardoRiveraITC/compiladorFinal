from lark import Lark, Transformer, tree, v_args

class parc:
    
    def __init__(self,grammar,stable,mode):
        self.grammar=grammar
        self.stable=stable
        self.mode=mode

    def start(self):
        calc_parser = Lark(self.grammar, parser='lalr')
        calc = calc_parser.parse
        tok=''
        for i in range(1,len(self.stable.getTable())+1):
            refIdx=self.stable.getTable()[i]["reference"]
            if(refIdx is not ''):
                tok+=(self.stable.getTable()[refIdx]["token"])
            else:
                tok +=self.stable.getTable()[i]["token"]
        print(tok)
        print(calc(str(tok)).pretty())


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    #number = float

    def __init__(self):
        self.vars = {}
