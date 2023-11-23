import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
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


#cuando abras un archivo o se de al boton de iniciar analisis


#los objetos de tabla de simbolos y el stack de errores ya estan llenados desde el objeto, en este caso son stable y errorS
symbolTableGlobal(stable)
errorStack(errorS)




class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1100x500")
        self.title("115")

        

        self.editor = ScrolledText(self, wrap=tk.WORD, width=50, height=20, font=("Courier New", 12))
        self.editor.place(x=25, y=25)

        self.tabla = ttk.Treeview(self, columns=("Id", "Token", "Lexema",), show="headings")
        self.tabla.heading("Id", text="Id")
        self.tabla.heading("Token", text="Token")
        self.tabla.heading("Lexema", text="Lexema")
        
        self.tabla.place(x=600, y=25, width=600, height=400)

        #para la tabla de los errores
        
        self.error = ttk.Treeview(self, columns=("Id", "Error"), show="headings")
        self.error.heading("Id", text="Id")
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
        file = './Programa.txt'  # ruta
        test = lex(self.editor.get("1.0", tk.END), mode, stable, errorS)
        test.startLexer()

        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla antes de agregar nuevos datos
        for row, (token, lexema) in enumerate(test.campo1):
            self.tabla.insert("", "end", values=(row + 1, token, lexema))

        messagebox.showinfo("Análisis Léxico", "Se ha completado el análisis léxico y se han mostrado los resultados en la tabla.")
            
    
        
        
        #analisis = analisisl()
        #analisis.ruta = self.path
        #analisis.a()
        #self.tabla.delete(*self.tabla.get_children())
        #for row, e in enumerate(analisis.campo1):
           # self.tabla.insert("", "end", values=(analisis.campo1[row], analisis.campo2[row], analisis.campo3[row], analisis.campo4[row]))

    def analisis_sintactico(self):
        # Implementación del análisis sintáctico
        messagebox.showinfo("Análisis Sintáctico", "Aquí va la implementación del análisis sintáctico")

    def analisis_semantico(self):
        # Implementación del análisis semántico
        messagebox.showinfo("Análisis Semántico", "Aquí va la implementación del análisis semántico")

    def dialog_critical(self, s):
        messagebox.showerror("Error", s)

    def file_open(self):
        path = filedialog.askopenfilename(filetypes=[("Text documents", "*.txt"), ("All files", "*.*")])
        if path:
            try:
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
