import tkinter as tk
from tkinter import filedialog


def archivo_nuevo_presionado(event=None):
    print("¡Has presionado para crear un nuevo archivo!")

def menu_iniciar_con_sistema_presionado():
    if iniciar_con_sistema.get():
        print("Opción establecida (iniciar con el sistema).")
    else:
        print("Opción deshabilitada (no iniciar con el sistema).")

# FUNCION PARA ABRIR ARCHIVO
def abrir_archivo():
    archivo_abierto = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo_abierto:
        with open(archivo_abierto, 'r') as file:
            contenido = file.read()

        # Limpiar las áreas de texto antes de cargar nuevo contenido
        area_texto1.delete(1.0, tk.END)
        area_texto2.delete(1.0, tk.END)
        area_texto3.delete(1.0, tk.END)

        # Colocar el contenido en las áreas de texto
        area_texto1.insert(tk.END, contenido)
        area_texto2.insert(tk.END, contenido)
        area_texto3.insert(tk.END, contenido)

        print(f"Abrir archivo: {archivo_abierto}")

# FUNCION PARA GUARDAR ARCHIVO
def guardar_archivo():
    archivo_guardado = filedialog.asksaveasfilename(title="Guardar archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo_guardado:
        print(f"Guardar archivo: {archivo_guardado}")


def menu_tema_presionado():
    valor_tema = tema_elegido.get()
    if valor_tema == 1:
        print("Tema claro establecido.")
    elif valor_tema == 2:
        print("Tema oscuro establecido.")
ventana = tk.Tk()
ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
#img_menu_nuevo = tk.PhotoImage(file="C:/Users/luisa/OneDrive/Documentos/LENGUAJES Y AUTOMATAS 2 CON RGG/nuevo_archivo.png")

menu_ayuda = tk.Menu(barra_menus, tearoff=False)

menu_ayuda.add_command(
    label="About",
    accelerator="Ctrl+N",
    command=archivo_nuevo_presionado,
    #image=img_menu_nuevo,
    compound=tk.LEFT

    
)
#MENU DESPLEGABLE DE ARCHIVO



menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=archivo_nuevo_presionado,
    #image=img_menu_nuevo,
    compound=tk.LEFT

    
)

menu_archivo.add_command(
    label="Abrir",
    accelerator="Ctrl+O",
    command=abrir_archivo,
    #image=img_menu_nuevo,
    compound=tk.LEFT

    
)

menu_archivo.add_command(
    label="Guardar",
    accelerator="Ctrl+G",
    command=abrir_archivo,
    #image=img_menu_nuevo,
    compound=tk.LEFT

    
)

menu_archivo.add_command(
    label="Salir",
    accelerator="Alt+F4",
    command=ventana.destroy,
    #image=img_menu_nuevo,
    compound=tk.LEFT

    
)
#AQUI ACABAN LAS OPCIONES DEL MENU DE ARCHIVO...

ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
#OPCIONES DEL MENU DE OPCIONES
menu_opciones.add_command(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    
)

menu_opciones.add_command(
    label="Analisis Lexico",
    command=menu_iniciar_con_sistema_presionado,
    
)

menu_opciones.add_command(
    label="Analisis Sintactico",
    command=menu_iniciar_con_sistema_presionado,
    
)

menu_opciones.add_command(
    label="Analisis Semantico",
    command=menu_iniciar_con_sistema_presionado,
    
)

# Áreas de texto derecha
area_texto1 = tk.Text(ventana, height=50, width=30)
area_texto1.pack(pady=10, side="right")

#abajo
area_texto2 = tk.Text(ventana, height=10, width=120)
area_texto2.pack(pady=10, side="bottom")

# en medio
area_texto3 = tk.Text(ventana, height=30, width=120)
area_texto3.pack(pady=10, side="top")


menu_tema = tk.Menu(barra_menus, tearoff=False)
tema_elegido = tk.IntVar()
tema_elegido.set(1)  # Opción seleccionada por defecto ("Claro").
menu_tema.add_radiobutton(
    label="Claro",
    variable=tema_elegido,
    value=1,
    command=menu_tema_presionado
)
menu_tema.add_radiobutton(
    label="Oscuro",
    value=2,
    variable=tema_elegido,
    command=menu_tema_presionado
)
menu_opciones.add_cascade(menu=menu_tema, label="Tema")
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")

ventana.config(menu=barra_menus)
ventana.geometry("1080x1024")
ventana.mainloop()