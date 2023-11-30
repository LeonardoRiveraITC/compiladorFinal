import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from parser import *
import time as time
import os


from scan import limpiarWhite
from lexDFA import * 
from symbolTable import *
from state import *
import sys
sys.path.append('../utilities/')
from errorStack import *
from lex import *
from symbolTable import symbolTableGlobal

stable=symbolTableGlobal({})
#modo
mode=state(False)
#stack de errores
errorS=errorStack([])

grammar = """
    ?start: block 

    ?block: "{" ([decision] [iteracion] [decl])* "}"  

    ?decision: "si" "(" exprlog ")" block 

    ?iteracion: "mientras" "(" exprlog ")" block 

    ?exprlog: fact 
            | fact oplog fact

    ?fact: (FLOAT | NUM | CAD | ID )

    ?decl: [TIPODATO] ID ["=" (CAD|ID|[sum]*)] ";"

    ?sum: product
        | sum "+" product   
        | sum "-" product  

    ?product: atom
        | product "*" atom  
        | product "/" atom  

    ?atom: number | ID         

    number: (FLOAT|NUM)
    FLOAT: /(.*)/
    NUM: /(.*)/
 
    CAD: /(.*)/
    TIPODATO: /(.*)/
    ID:/(.*)/

    ?oplog: ">"  
        | EQEQ
        | "<"  
        | ">="
        | "<="  
    
    EQEQ: "=="
    
"""



myParse=parc(grammar,stable,mode,errorS)

class Photo:   
    def __init__(self, image):
        self.image = image
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()
    def widgets(self):
        self.img = PhotoImage(file=self.image)
        label = tk.Label(self.root, image=self.img)
        label.pack()


class MainWindow(tk.Tk):
    def __init__(self, file='',*args, **kwargs):
        self.file=file
        super().__init__(*args, **kwargs)
        self.geometry("1100x500")
        self.title("115")
        self.photo = tk.PhotoImage("./arbol.png")



        self.editor = ScrolledText(self, wrap=tk.WORD, width=50, height=20, font=("Courier New", 12))
        self.editor.place(x=25, y=25)

        self.tabla = ttk.Treeview(self, columns=("Id", "Token", "Lexema","Referencia",), show="headings")
        self.tabla.heading("Id", text="Id")
        self.tabla.heading("Token", text="Token")
        self.tabla.heading("Lexema", text="Lexema")
        self.tabla.heading("Referencia", text="Referencia")

        self.tabla.place(x=600, y=25, width=800, height=400)

        #para la tabla de los errores

        self.error = ttk.Treeview(self, columns=("Id", "Error"), show="headings")
        self.error.heading("Id", text="No.")
        self.error.heading("Error", text="Error")

        self.error.place(x=30, y=500, width=1200, height=800)

        #fin de la tabla de los errores


        self.boton_analisis_lexico = tk.Button(self, text="Análisis Léxico", command=self.analisis_lexico)
        self.boton_analisis_lexico.place(x=40, y=450)

        self.boton_analisis_sintactico = tk.Button(self, text="Análisis Sintáctico", command=self.analisis_sintactico)
        self.boton_analisis_sintactico.place(x=160, y=450)

        self.boton_analisis_semantico = tk.Button(self, text="Análisis Semántico", command=self.analisis_semantico)
        self.boton_analisis_semantico.place(x=280, y=450)

        self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abrir Archivo", command=self.file_open)
        file_menu.add_command(label="Guardar", command=self.file_save)
        file_menu.add_command(label="Guardar como", command=self.file_saveas)
        file_menu.add_command(label="Imprimir", command=self.file_print)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        self.config(menu=menubar)

        self.path = None

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.update_title()
        self.mainloop()

    def analisis_lexico(self):
        print(self.path)
        self.file_save()
        stable.clean()
        errorS.cleanErrorStack()
        test = lex(self.file, mode, stable, errorS)
        test.startLexer()
        
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla antes de agregar nuevos datos
        self.error.delete(*self.error.get_children())  # Limpiar la tabla antes de agregar nuevos datos
        for i in range(1,len(stable.getTable())):
            self.tabla.insert("", "end", values=(i, stable.getTable()[i]["token"],stable.getTable()[i]["lex"],stable.getTable()[i]["reference"]))

        for i in range(0,len(errorS.getErrorStack())):
            self.error.insert("","end",values=(i,errorS.getErrorStack()[i]))

        messagebox.showinfo("Análisis Léxico", "Se ha completado el análisis léxico y se han mostrado los resultados en la tabla.")


        #analisis = analisisl()
        #analisis.ruta = self.path
        #analisis.a()
        #self.tabla.delete(*self.tabla.get_children())
        #for row, e in enumerate(analisis.campo1):
           # self.tabla.insert("", "end", values=(analisis.campo1[row], analisis.campo2[row], analisis.campo3[row], analisis.campo4[row]))

    def analisis_sintactico(self):
        # Implementación del análisis sintáctico
        myParse.start()
        messagebox.showinfo("Análisis Sintáctico")
        for i in range(0,len(errorS.getErrorStack())):
            self.error.insert("","end",values=(i,errorS.getErrorStack()[i]))

    def analisis_semantico(self):
        # Implementación del análisis semántico
        myParse.sem()
        messagebox.showinfo("Análisis Semántico", "Aquí va la implementación del análisis semántico")
        for i in range(0,len(errorS.getErrorStack())):
            self.error.insert("","end",values=(i,errorS.getErrorStack()[i]))

    def dialog_critical(self, s):
        messagebox.showerror("Error", s)

    def file_open(self):
        path = filedialog.askopenfilename(filetypes=[("Text documents", "*.txt"), ("All files", "*.*")])
        if path:
            try:
                self.file=path
                with open(path, 'r') as f:
                    text = f.read()
            except Exception as e:
                self.dialog_critical(str(e))
            else:
                self.path = path
                self.editor.delete(1.0, tk.END)
                self.editor.insert(tk.END, text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            return self.file_saveas()
        self._save_to_path(self.path)

    def file_saveas(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text documents", "*.txt"), ("All files", "*.*")])
        if not path:
            return
        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.get(1.0, tk.END)
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.update_title()

    def file_print(self):
        # Implementación de la impresión
        pass

    def update_title(self):
        self.title("%s - Tkinter Notepad" % (os.path.basename(self.path) if self.path else "Untitled"))

    def on_close(self):
        self.destroy()

if __name__ == '__main__':
    window = MainWindow()
