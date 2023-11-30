from lark import Lark, Transformer, Visitor, tree, v_args
from lark.lexer import Lexer,Token
from pydot import *

class parc:
    
    def __init__(self,grammar,stable,mode):
        self.grammar=grammar
        self.stable=stable
        self.mode=mode


    def start(self):
        calc_parser = Lark(self.grammar, parser='lalr')
        data=''
        for i in range(1,len(self.stable.getTable())+1):
            refIdx=self.stable.getTable()[i]["reference"]
            if(refIdx != ''):
                tok=(Token (self.stable.getTable()[refIdx]["lex"],self.stable.getTable()[refIdx]["token"],line=self.stable.getTable()[i]["line"]))
                data+=tok

            else:
                tok=(Token (self.stable.getTable()[i]["lex"],self.stable.getTable()[i]["token"],line=self.stable.getTable()[i]["line"]))
                data+=tok
        print(data)
        ast=calc_parser.parse(str(data))
        print(ast.pretty())
        
        transf=CalculateTree()
        transf.visit(ast)
        make_png('./arbol.png',ast)


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Visitor):
    from operator import add, sub, mul, truediv as div, neg
    atom=float

    def decl(tipo,id):
        print(id)
        
def make_png(filename,parser):
    tree.pydot__tree_to_png( parser, filename)
