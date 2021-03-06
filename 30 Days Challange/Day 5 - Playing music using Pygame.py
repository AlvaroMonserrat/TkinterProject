#
# Day 5: Reproduciondo musica usando Pygame
# 28.12.19
#

import tkinter
from pygame import mixer


def play_music():
    mixer.music.load("sound.mp3")
    mixer.music.play()


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

    # Button
    play_photo = tkinter.PhotoImage(file='play.png')
    play_btn = tkinter.Button(root, image=play_photo, command=play_music)
    play_btn.pack()

    root.mainloop()


if __name__ == '__main__':
    main()

