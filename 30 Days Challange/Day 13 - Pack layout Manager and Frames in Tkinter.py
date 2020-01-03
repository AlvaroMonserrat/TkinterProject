#
# Day 13: Administrador de Frame
# 02.01.20
#

import tkinter
from tkinter import messagebox
from tkinter import filedialog
from pygame import mixer


def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = False
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
        except NameError:
            tkinter.messagebox.showerror("No Music", "No se encontro archivo de sonido.")
            print("Error")


paused = False


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"
    paused = True


def set_volume(val):
    volume = int(val) / 100
    # set_volume toma valores entre 0 y 1.
    mixer.music.set_volume(volume)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python')


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


def main():
    root = tkinter.Tk()

    # Creando barra de menu
    menubar = tkinter.Menu(root)
    root.config(menu=menubar)

    # Creando sub menu File(Open, Exit)
    subMenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open", command=browse_file)
    subMenu.add_command(label="Exit", command=root.destroy)

    # Creando sub menu Help(About Us)
    subMenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us", command=about_us)

    # init Mixer
    mixer.init()

    # Set window parameters
    root.geometry('800x600')
    root.title('Melody')
    root.iconbitmap('fono.ico')

    # Add widgets
    label_text = tkinter.Label(root, text='Reproductor de musica')
    label_text.pack()

    # Frame
    middle_frame = tkinter.Frame(root)
    middle_frame.pack(padx=10, pady=10)

    # Add Button Play
    play_photo = tkinter.PhotoImage(file='play.png')
    play_btn = tkinter.Button(middle_frame, image=play_photo, command=play_music)
    play_btn.pack()

    # Add Button Paused
    pause_photo = tkinter.PhotoImage(file='paused.png')
    paused_btn = tkinter.Button(middle_frame, image=pause_photo, command=pause_music)
    paused_btn.pack(side=tkinter.LEFT)

    # Add Button Stop
    stop_photo = tkinter.PhotoImage(file='stop.png')
    stop_btn = tkinter.Button(middle_frame, image=stop_photo, command=stop_music)
    stop_btn.pack()

    # Add Scale Volume
    scale = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL, command=set_volume, length=300)
    scale.set(70)
    scale.pack()

    # Creando StatusBaR
    global statusbar
    statusbar = tkinter.Label(root, text="Welcome to Melody", relief=tkinter.SUNKEN, anchor=tkinter.W)
    statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    root.mainloop()


if __name__ == '__main__':
    main()
