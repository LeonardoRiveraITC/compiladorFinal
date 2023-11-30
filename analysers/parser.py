from lark import exceptions, Lark, Transformer, Visitor, tree, v_args
from lark.lexer import Lexer,Token
from pydot import *

class parc:
    
    def __init__(self,grammar,stable,mode,estack):
        self.grammar=grammar
        self.stable=stable
        self.mode=mode
        self.estack=estack


    def start(self):
        try:
            calc_parser = Lark(self.grammar, parser='lalr',lexer=TypeLexer,propagate_positions=True)
            #calc_parser=calc_parser.parse_interactive()
            ast=calc_parser.parse(self.stable)
            calc_parser.parse
                    #calc_parser.feed_token(tok)
            #print(ast.pretty())
            
            make_png('./arbol.png',ast)
        except exceptions.UnexpectedToken as e:
            print(e)
            self.estack.pushErrorStack(200,e)

    def sem(self):
            calc_parser = Lark(self.grammar, parser='lalr',lexer=TypeLexer,propagate_positions=True)
            ast=calc_parser.parse(self.stable)
            transf=CalculateTree(self.estack)
            transf=transf.transform(ast)


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    
    def __init__(self,estack):
        self.vars = {}
        self.estack=estack

    @v_args(meta=True)    # Affects the signatures of the methods
    def decl(self, a1,a2):
        numb=["number","NUM","FLOAT","product","sum","atom","entero","float"]
        if(a2[0] is not None):
            self.vars[a2[1].value]=a2[0].value
        else:
            if(a2[1].value not in self.vars):
                self.estack.pushErrorStack(301,a2[1].line)
            else:
                if(self.vars[a2[1].value] in numb):
                    if(isinstance(a2[2], str)):
                        self.estack.pushErrorStack(302,a2[1].line)
                elif(not isinstance(a2[2],str)):
                        self.estack.pushErrorStack(303,a2[1].line)

    @v_args(meta=True)
    def exprlog(self,a1,a2):
        numb=["number","NUM","FLOAT","product","sum","atom","entero","float"]
        if(a2[0].type == "ID"):
            if(a2[0].value not in self.vars):
                self.estack.pushErrorStack(304,a2[0].line)
            elif(a2[0] in self.vars):
                if(self.vars[a2[0]] in numb):
                    if(a2[2].type not in numb):
                        if(a2[2].type != "NUM"):
                            self.estack.pushErrorStack(305,a2[0].line)
                elif(not isinstance(a2[2],str)):
                        self.estack.pushErrorStack(306,a2[1].line)

        elif(a2[0].type in numb):
            if(a2[2].type not in numb):
                if(a2[2].type != "NUM"):
                    self.estack.pushErrorStack(305,a2[0].line)
        elif(not isinstance(a2[2],str)):
                self.estack.pushErrorStack(306,a2[1].line)
        
def make_png(filename,parser):
    tree.pydot__tree_to_png( parser, filename)

class TypeLexer(Lexer):
    def __init__(self, lexer_conf):
        pass

    def lex(self, data):
        for i in range(1,len(data.getTable())+1):
            refIdx=data.getTable()[i]["reference"]
            if(refIdx != ''):
                tok=(Token (data.getTable()[refIdx]["token"],value=data.getTable()[refIdx]["lex"],line=data.getTable()[i]["line"]))
                yield tok
                #calc_parser.feed_token(tok)

            else:
                tok= (Token (data.getTable()[i]["token"],data.getTable()[i]["lex"],line=data.getTable()[i]["line"]))
                yield tok
