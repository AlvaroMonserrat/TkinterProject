#Gestor de geometria pack()

from tkinter import *
from tkinter import ttk, font
import  getpass

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")

        #Cambia la fuente actual a negrita
        fuente = font.Font(weight='bold')

        #Define las etiquetas que acompanan a las cajas de entrada
        self.etiq1 = ttk.Label(self.raiz, text="Usuario: ", font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Password: ", font=fuente)

        #Declara dos variables tipo string
        self.usuario = StringVar()
        self.clave = StringVar()

        #Realiza una lectura del nombre de usuario que inicio sesion en el sistema
        self.usuario.set(getpass.getuser())

        #Define dos textbox de entrada que aceptan cadenas de 30 caracteres max.
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30, show="*")

        #Linea separadora
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        #Se definen dos botones con dos metodos. El boton 'Aceptar' llama a self.aceptar'
        #el boton 'Cancelar' cierra la app.
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", command=quit)


        #Defina las posiciones de los widget dentro de la ventana
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

        #Foco a la caja de entrada de la contrasena
        self.ctext2.focus_set()

        self.raiz.mainloop()

    #Metodo para validar contrasena
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Password:  ", self.ctext2.get())
        else:
            print("Acceso denegado")

            self.clave.set("")
            self.ctext2.focus_set()



def main():
    mi_app = Aplicacion()
    return  0

if __name__ == '__main__':
    main()