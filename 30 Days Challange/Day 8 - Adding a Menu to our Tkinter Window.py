#
# Day 8: Agregando menu a la ventana
# 31.12.19
#


import tkinter
from pygame import mixer


def play_music():
    mixer.music.load("sound.mp3")
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def set_volume(val):
    volume = int(val) / 100
    # set_volume toma valores entre 0 y 1.
    mixer.music.set_volume(volume)


def main():
    root = tkinter.Tk()

    # Creando barra de menu
    menubar = tkinter.Menu(root)
    root.config(menu=menubar)

    # Creando sub menu File(Open, Exit)
    subMenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open")
    subMenu.add_command(label="Exit")

    # Creando sub menu Help(About Us)
    subMenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us")

    # init Mixer
    mixer.init()

    # Set window parameters
    root.geometry('800x600')
    root.title('Melody')
    root.iconbitmap('fono.ico')

    # Add widgets
    label_text = tkinter.Label(root, text='Reproductor de musica')
    label_text.pack()

    # Add Button Play
    play_photo = tkinter.PhotoImage(file='play.png')
    play_btn = tkinter.Button(root, image=play_photo, command=play_music)
    play_btn.pack()

    # Add Button Stop
    stop_photo = tkinter.PhotoImage(file='stop.png')
    stop_btn = tkinter.Button(root, image=stop_photo, command=stop_music)
    stop_btn.pack()

    # Add Scale Volume
    scale = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL, command=set_volume, length=300)
    scale.set(70)
    scale.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
