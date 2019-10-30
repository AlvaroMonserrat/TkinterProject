

from tkinter import *
from tkinter import ttk

#Crea una clase Python para definir la interfaz de usuario de
#la app. Cuando se cree un objeto de tipo 'Aplicacion' se
#ejecutara automaticamente el metodo __init__() que construye
# y muestra la ventana con todos sus widgets:

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('800x600')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicacion')
        ttk.Button(raiz, text='Salir', command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()

#Define la funcion main() que es en realidad la que indica el
#comienzo del programa. Dentro de ella se crea el objeto
#aplicacion 'mi_app' basado en la clase 'Aplicacion':

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()