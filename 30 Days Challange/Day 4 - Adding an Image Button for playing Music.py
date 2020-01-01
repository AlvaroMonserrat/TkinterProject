#
# Day 4: Agregando una imagen tipo Boton para reproducir musica
# 28.12.19
#

import tkinter


class WindowMain(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.root = root
        self.set_window_init()

        self.label_text = None
        self.play_photo = None
        self.button_play = None

        self.set_widgets()

    def set_window_init(self):
        self.root.title('MusicMix')
        self.root.geometry('800x600')
        self.root.iconbitmap('fono.ico')

    def set_widgets(self):
        self.label_text = tkinter.Label(self.root, text='Reproductor de Musica!')
        self.label_text.pack()

        self.play_photo = tkinter.PhotoImage(file='play.png')
        self.button_play = tkinter.Button(self.root, image=self.play_photo, command=self.play_btn)
        self.button_play.pack()

    @staticmethod
    def play_btn():
        print("Song!!...")


def main():
    root = tkinter.Tk()
    WindowMain(root)
    root.mainloop()


if __name__ == '__main__':
    main()

