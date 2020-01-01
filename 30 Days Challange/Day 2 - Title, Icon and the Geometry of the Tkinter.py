#
# Day 2: Titulo, icono y geometria de ventana en Tkinter
# 28.12.19
#

import tkinter


def main():
    root = tkinter.Tk()
    # Ajustar tamano de la ventana
    root.geometry("300x300")
    # Perzonalizar titulo ventana
    root.title("Music Mix")
    # Perzonalizar icono de la ventana
    root.iconbitmap(r'fono.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
