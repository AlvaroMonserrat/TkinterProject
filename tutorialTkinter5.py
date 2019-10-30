#Gestor de geometria grid()

from tkinter import *
from tkinter import ttk, font
import getpass


class Applicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")

        #Establece que no se modifica el tamano de la ventana
        self.raiz.resizable(0, 0)
        fuente = font.Font(weight='bold')

        #Define un widget de tipo 'Frame' (marco) que sera el
        #contenedor del resto de widgets.

        self.marco = ttk.Frame(self.raiz, borderwidth=20, relief="sunken" , padding=(20, 10))


        self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente, padding=(5, 5))
        self.etiq2 = ttk.Label(self.marco, text="Password:", font=fuente, padding=(5, 5))

        #resultado
        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.marco, textvariable=self.mensa, font=fuente, foreground='blue')

        #Variables para la textbox
        self.usuario = StringVar()
        self.clave = StringVar()

        #Usuario actual window
        self.usuario.set(getpass.getuser())

        #Textbox
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*", width=30)

        #Barra separadora
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)

        #Boton Aceptar
        self.boton1 = ttk.Button(self.marco, text="Aceptar", padding=(5, 5), command=self.aceptar)
        #Boton Cancelar
        self.boton2 = ttk.Button(self.marco, text="Cancelar", padding=(5, 5), command=quit)


        #columnspan indica cuantas columnas utilizara el widget
        self.marco.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3, sticky="we")
        self.etiq3.grid(column=0, row=4, columnspan=3)
        self.boton1.grid(column=1, row=5)
        self.boton2.grid(column=2, row=5)

        #Foco en la clave
        self.ctext2.focus_set()

        #El metodo 'bind()' asocia el evento de hacer clic con el boton izquierdo
        self.ctext2.bind('<Button-1>', self.borrar_mensa)

        self.raiz.mainloop()


    def aceptar(self):
        if self.clave.get() == "tkinter":
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Acceso Permitdo")
            print("Bienvenido ", self.ctext1.get())
        else:
            print("Acceso Denegado")
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso Denegado")
            self.clave.set("")
            self.ctext2.focus_set()

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")

def main():
    mi_app = Applicacion()
    return 0

if __name__ == '__main__':
    main()