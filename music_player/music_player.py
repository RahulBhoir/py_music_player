import tkinter as tk
from tkinter import StringVar, filedialog
from tkinter.constants import ACTIVE, BOTH, END, RIGHT
from pygame import mixer
import os

WIDTH = 70
HEIGHT = 50
FONT_STYLE = 'consolas'
FONT_SIZE = 18
BUTTON_FONT = (FONT_STYLE, FONT_SIZE, 'bold')
LABEL_FONT = (FONT_STYLE,  FONT_SIZE, 'bold')


class MusicPlayer():
    def __init__(self, root):
        root.geometry('600x200')
        root.resizable(0, 0)
        root.title('Music Player')

        self.music_folder_path = ''
        self.music_file_name = StringVar()
        self.song_state = False
        self.music_files = []

        # for displaying song name
        self.track_name = tk.Label(root, text='Welcome!', font=LABEL_FONT,
                                   bg='light blue', justify='center')
        self.track_name.place(x=0, y=0, width=400, height=100)

        # load button
        self.load_btn = tk.Button(root, text='load', font=BUTTON_FONT,
                                  command=self.loadSong)
        self.load_btn.place(x=300, y=120, width=WIDTH, height=HEIGHT)

        # play button
        self.play_btn = tk.Button(root, text='play', font=BUTTON_FONT,
                                  command=self.playSong)
        self.play_btn.place(x=10, y=120, width=WIDTH, height=HEIGHT)

        # pause button
        self.pause_btn = tk.Button(
            root, text='pause', font=BUTTON_FONT, command=self.pauseSong)
        self.pause_btn.place(x=90, y=120, width=WIDTH+30, height=HEIGHT)

        # stop button
        self.stop_btn = tk.Button(
            root, text='stop', font=BUTTON_FONT, command=self.stopSong)
        self.stop_btn.place(x=200, y=120, width=WIDTH, height=HEIGHT)

        # labe frame for track list
        self.song_list_label_frame = tk.LabelFrame(
            root, text='track list', font=(FONT_STYLE, 12))
        self.song_list_label_frame.place(
            x=400, y=0, width=200, height=200)

        # track list box
        self.song_list_box = tk.Listbox(
            self.song_list_label_frame, selectmode='SINGLE')
        self.song_list_box.bind('<Button-1>', self.playSong)
        self.song_list_box.place(x=400, y=0, width=200, height=200)

        # scroll bar for track list
        self.scroll_bar = tk.Scrollbar(root)
        self.scroll_bar.pack(side=RIGHT, fill=BOTH)
        self.song_list_box.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.song_list_box.yview)

    def loadSong(self):
        # getting the music folder path
        self.music_folder_path = filedialog.askdirectory() + '/'
        # getting the track list from the music folder
        self.music_files = os.listdir(self.music_folder_path)
        # displaying the track list in the list box
        for file in self.music_files:
            self.song_list_box.insert(END, file)

    def playSong(self):
        # to get the song name from the songs list
        self.music_file = self.song_list_box.get(ACTIVE)
        # displaying song name in the label box
        self.track_name['text'] = self.music_file
        # playing the song
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_folder_path + self.music_file)
            mixer.music.play()
            self.song_state = True

    def pauseSong(self):
        if self.song_state:
            mixer.music.pause()
            # for changing the button text to unpause
            self.pause_btn['text'] = 'unpause'
            self.song_state = False
        else:
            mixer.music.unpause()
            # for changing the button text to pause
            self.pause_btn['text'] = 'pause'
            self.song_state = True

    def stopSong(self):
        # stop the song
        mixer.music.stop()
        self.song_state = False


root = tk.Tk()
MusicPlayer(root)
root.mainloop()
