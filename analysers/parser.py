from lark import Lark, Transformer, tree, v_args


try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

"""
@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)

"""
calc_grammar = """
    ?start: block 

    ?block: [ (decl ";")* | decision* | iteracion* ] 

    ?decision: "si" "(" exprlog ")" "{" block "}"

    ?iteracion: "mientras" "(" exprlog ")" "{" block "}"

    ?exprlog: fact 
            | fact oplog fact

    ?fact: number | cadena | id

    ?decl: tipodato id ["=" number|cadena|id|sum]
        | id "=" number|cadena|id|sum 

    ?sum: product
        | sum "+" product   
        | sum "-" product  

    ?product: atom
        | product "*" atom  
        | product "/" atom  

    ?atom: number          
         | "-" atom         -> neg
         | "(" sum ")"

    number: "float"|"num"
    cadena: "cad"
    tipodato: "cadena"| "flotante" | "entero"
    id:"id"

    oplog: ">"  
        | "<"  
        | ">="
        | "<="  
        | "==" 

"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    #number = float

    def __init__(self):
        self.vars = {}



calc_parser = Lark(calc_grammar, parser='lalr')
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(str(s)).pretty())
        res = CalculateTree().transform(calc(s))
        print(res)


if __name__ == '__main__':
    # test()
    main()
