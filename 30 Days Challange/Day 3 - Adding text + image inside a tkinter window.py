#
# Day 3 - Incluir texto e imagen dentro de la ventana
# 28.12.19
#

import tkinter


def main():
    root = tkinter.Tk()
    root.geometry('800x600')
    root.title('Melody')
    root.iconbitmap('fono.ico')

    label_text = tkinter.Label(root, text='Lets make some noise!')
    label_text.pack()

    play_photo = tkinter.PhotoImage(file='play.png')
    label_photo = tkinter.Label(root, image=play_photo)
    label_photo.pack()

    root.mainloop()


if __name__ == '__main__':
    main()


