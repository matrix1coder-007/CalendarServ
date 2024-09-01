import pyttsx3
import os
import time
from pygame import mixer
from datetime import datetime
from tkinter.constants import CENTER, LEFT, RIGHT
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import *

def play_welcome_msg():
    engine = pyttsx3.init()
    engine.say('Good morning, Namaste, Welcome you all!')
    engine.runAndWait()

def readable_date_info(date):
    return date.ctime()

def play_songs():
    x = [dirs for dirs in os.listdir(os.getcwd())]
    if 'songs' not in x:
        os.makedirs('songs')

    songs = []
    try:
        songs_folder = os.path.join(os.getcwd(), 'songs')
        for files in os.listdir(songs_folder):
            if files.endswith('.mp3'):
                songs.append(files)
    except OSError:
        pass    

    for song in songs:
        mixer.init()
        mixer.music.load(os.path.join(os.getcwd()+'//songs', song))
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(5)

def open_calendar():
    pass

r = tk.Tk()
r.iconbitmap('icon.ico')
width= r.winfo_screenwidth() 
height= r.winfo_screenheight()
r.geometry("%dx%d" % (width, height))
r.title('IK TechServe')
r.configure(background='lightseagreen')

play_welcome_msg()

today_date = readable_date_info(datetime.now())
today_panel = Label(r, text = today_date, font =('Jokerman', 35), foreground='white', background='lightseagreen')
today_panel.pack(padx=30, pady=20)

file = Image.open('Welcome-4.png')

pixels_x, pixels_y = int(0.9*file.size[0]), int(0.8*file.size[1]) 
img = ImageTk.PhotoImage(file.resize((pixels_x, pixels_y)))
panel = Label(r, image = img, borderwidth=0, relief='flat')
panel.pack(pady=20)

bhajan_serve = tk.Button(r, text="Bhajan/Songs", fg='whitesmoke', bg='lightseagreen', font=('Jokerman', 30), command=play_songs)
bhajan_serve.pack(side=LEFT, padx=20, pady=10)

calendar_serve = tk.Button(r, text="Calendar", fg='whitesmoke', bg='lightseagreen', font=('Jokerman', 30), command=open_calendar)
calendar_serve.pack(side=RIGHT, padx=20, pady=10)

r.mainloop()