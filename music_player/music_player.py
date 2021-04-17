import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import re

HEIGHT = 0
WIDTH = 0
BUTTON_FONT = ('arial', 18, 'bold')
LABEL_FONT = ('arial', 18, 'bold')


class MusicPlayer():
    def __init__(self, root):
        root.geometry('300x220')
        root.resizable(0, 0)
        root.title('Music Player')

        self.label_btn = tk.Label(root, text='', font=LABEL_FONT,
                                  bg='light blue', width=20, height=2, justify='center')
        self.label_btn.grid(columnspan=6)

        self.load_btn = tk.Button(root, text='load', font=BUTTON_FONT, width=WIDTH,
                                  height=HEIGHT, command=self.loadSong)
        self.load_btn.grid(row=1, column=1)

        self.play_btn = tk.Button(root, text='play', font=BUTTON_FONT, width=WIDTH,
                                  height=HEIGHT, command=self.playSong)
        self.play_btn.grid(row=2, column=0)

        self.pause_btn = tk.Button(root, text='pause', font=BUTTON_FONT, width=WIDTH,
                                   height=HEIGHT, command=self.pauseSong)
        self.pause_btn.grid(row=2, column=2)

        self.stop_btn = tk.Button(root, text='stop', font=BUTTON_FONT, width=WIDTH,
                                  height=HEIGHT, command=self.stopSong)
        self.stop_btn.grid(row=3, column=1)

        self.music_file = False
        self.song_state = False

    def songName(self):
        if self.music_file:
            file_name = str(self.music_file).split('/')[-1].split('.mp3')[0]
            self.label_btn['text'] = file_name

    def loadSong(self):
        self.music_file = filedialog.askopenfile()
        self.songName()

    def playSong(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.song_state = True

    def pauseSong(self):
        if self.song_state:
            mixer.music.pause()
            self.song_state = False
        else:
            mixer.music.unpause()
            self.song_state = True

    def stopSong(self):
        mixer.music.stop()
        self.song_state = False


root = tk.Tk()
MusicPlayer(root)
root.mainloop()
