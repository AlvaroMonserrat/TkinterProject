#
# Day 6: Detener musica usando Pygame
# 31.12.19
#

import tkinter
from pygame import mixer


def play_music():
    mixer.music.load("sound.mp3")
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def main():
    root = tkinter.Tk()

    # Inicializar mixer
    mixer.init()

    # Set window parameters
    root.geometry('800x600')
    root.title('Melody')
    root.iconbitmap('fono.ico')

    # Add widgets
    label_text = tkinter.Label(root, text='Reproductor de musica')
    label_text.pack()

    # Add Button Play
    # Button
    play_photo = tkinter.PhotoImage(file='play.png')
    play_btn = tkinter.Button(root, image=play_photo, command=play_music)
    play_btn.pack()

    # Add Button Stop
    # Button
    stop_photo = tkinter.PhotoImage(file='stop.png')
    stop_btn = tkinter.Button(root, image=stop_photo, command=stop_music)
    stop_btn.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
