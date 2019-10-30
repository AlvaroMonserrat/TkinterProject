

from tkinter import *
from tkinter import ttk



class Aplicacion():
    def __init__(self):
        #El uso de self permite acceder a valores de la clase applicacion
        #desde otro metodo
        self.raiz = Tk()
        self.raiz.geometry('800x600+547+249')


        #Impide que el tamano de la ventana pueda modificarse
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Ver info')

        #Define el widget Text en el que se pueden introducir varias lineas de texto
        self.tinfo = Text(self.raiz, width=80, height=20)

        #Situa la caja en la parte superior de la ventana
        self.tinfo.pack(side=TOP)

        #Define el widget button 'self.binfo' que llamara al metodo 'self.verinfo'
        self.binfo = ttk.Button(self.raiz, text='Info', command=self.verinfo)

        #Colocar el boton 'self.binfo' debajo y a la izquierda del widget anterior
        self.binfo.pack(side=LEFT)

        #defini el boton 'self.bsalir'
        self.bsalir = ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy)

        #colocar el boton 'self.bsalir' a la derecha del objeto anterior
        self.bsalir.pack(side=RIGHT)

        #Resaltar el boton info
        self.binfo.focus_set()
        self.raiz.mainloop()

    def verinfo(self):
        #Borra el contenido que tenga la caja de texto
        self.tinfo.delete("1.0", END)

        #Obtiene informacion de la ventana 'self.raiz'
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()

        #Construye una cadena de texto con toda la informacion obtenida
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolucion y posicion: " + info2 + "\n"
        #Insertar la informacion en la caja de texto

        self.tinfo.insert("1.0", texto_info)


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == "__main__":
    main()