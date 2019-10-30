# Ventanas de aplicacion y dialogo

from tkinter import *
from tkinter import ttk


class Aplicacion():
    '''Clase Aplicacion'''
    # Declarar una variable de clase para contar ventas
    ventana = 0

    # Declarar una variable para el calculo de la posicion
    # de la ventana
    posx_y = 0

    def __init__(self):
        '''Construye vetana de aplicacion'''
        self.raiz = Tk()
        self.raiz.geometry('800x600+600+200')
        self.raiz.resizable(0, 0)
        self.raiz.title("Ventana de aplicacion")

        #Define boton Abrir
        self.boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
        self.boton.pack(side=BOTTOM, padx=20, pady=250)

        self.raiz.mainloop()

    def abrir(self):
        '''Construye una ventana de Dialogo'''
        #Define una nueva ventana de dialago
        self.dialogo = Toplevel()
        #Incrementa en 1 el cotnador de vetanas
        Aplicacion.ventana += 1

        #Recalcula la posicion de la ventana
        Aplicacion.posx_y += 50
        tamypos = '500x300+'+str(Aplicacion.posx_y)+'+'+str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)

        #Obtiene el identificaodr de la nueva ventana
        ident = self.dialogo.winfo_id()

        #Construye mensaje de la barra de titulo
        titulo = str(Aplicacion.ventana)+": "+str(ident)
        self.dialogo.title(titulo)

        #Crear Boton
        self.botonCerrar =ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
        self.botonCerrar.pack(side=BOTTOM, padx=20, pady=20)

        #Crear Label
        self.label1 = ttk.Label(self.dialogo, text='Ventana de Dialogo: Presione Cerrar para salir')
        self.label1.config(font=("Arial", 16))
        self.label1.pack(padx=20, pady=100)

        #Convierte el dialogo en ventana transitoria, la ventana master
        #Siempre se mantendra por detras
        self.dialogo.transient(master=self.raiz)

        #Permite trabajar con ventana tip Modal. queda bloqueda la
        #ventana principal
        self.dialogo.grab_set()

        self.raiz.wait_window(self.dialogo)


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
