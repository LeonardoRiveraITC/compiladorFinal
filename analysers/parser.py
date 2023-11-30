from lark import Lark, Transformer, Visitor, tree, v_args
from lark.lexer import Lexer,Token
from pydot import *

class parc:
    
    def __init__(self,grammar,stable,mode):
        self.grammar=grammar
        self.stable=stable
        self.mode=mode


    def start(self):
        calc_parser = Lark(self.grammar, parser='lalr',lexer=TypeLexer,propagate_positions=True)
        #calc_parser=calc_parser.parse_interactive()
        calc_parser.parse
                #calc_parser.feed_token(tok)
        ast=calc_parser.parse(self.stable)
        #print(ast.pretty())
        
        transf=CalculateTree()
        transf=transf.transform(ast)
        make_png('./arbol.png',ast)


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    
    def __init__(self):
        self.vars = {}

    @v_args(meta=True)    # Affects the signatures of the methods
    def decl(self, a1,a2):
        if(a2[0] is not None):
            print (a2[1])
            self.vars[a2[1].value]=a2[0].value
            print(self.vars)
        
def make_png(filename,parser):
    tree.pydot__tree_to_png( parser, filename)

class TypeLexer(Lexer):
    def __init__(self, lexer_conf):
        pass

    def lex(self, data):
        for i in range(1,len(data.getTable())+1):
            refIdx=data.getTable()[i]["reference"]
            if(refIdx != ''):
                tok=(Token (data.getTable()[refIdx]["token"],value=data.getTable()[refIdx]["lex"],line=i))
                yield tok
                #calc_parser.feed_token(tok)

            else:
                tok= (Token (data.getTable()[i]["token"],data.getTable()[i]["lex"],line=i))
                yield tok
