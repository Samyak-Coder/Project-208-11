import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

import ftplib
from ftplib import FTP

import os
import ntpath 
from tkinter import filedialog

from pathlib import Path

from playsound import playsound
import pygame
from pygame import mixer

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

listBox = None

song_selected  = 0

def play():
    global song_selected
    song_selected = listBox.get(ANCHOR) 
    
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")


def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_file/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def resume():
    global song_selected
    mixer.int()
    mixer.music.load('shared_file/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()

def browseFile():
    global Listbox
    global song_counter
    global filePathLabel

    try:
        filename = filedialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "ldftpd"

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        
        fname = ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)

        ftp_server.dir()
        ftp_server.quit()
    except FileNotFoundError:
        print("Cancle Button Pressed")

def musicWindow():
    global song_counter
    global infoLabel

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listBox.insert(song_counter, filename)
        song_counter += 1

    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, 
                        text = "Select Song",
                        bg="LightSkyBlue",
                        font=("Calibri", 0))
    selectLabel.place(x=2, y=1)

    listBox = Listbox(window,
                      height=10,
                      width=39,
                      activestyle="dotbox",
                      bg= "LightSkyBlue")
    listBox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listBox.yview)

    playButton = Button(window, 
                        text="Play",
                        width=10, 
                        bd=1, 
                        bg="SkyBlue",
                        activestyle="dotbox",
                        font=("Calibri",10))
    playButton.place(x=30, y=200)    

    stop = Button(window,
                  text="Stop",
                  bd=1,
                  width=10,
                  bg="SkyBlue",
                  font=("Calibri", 10))
    stop.place(x=200, y=200)

    upload = Button(window,
                  text="Upload",
                  bd=1,
                  width=10,
                  bg="SkyBlue",
                  font=("Calibri", 10))
    upload.place(x=30, y=250)

    infoLabel = Label(window, 
                      text="",
                      fg="blue",
                      font=("Calibri", 0))
    infoLabel.place(x=4, y=200)

    ResumeBtn = Button(window, text="Resume", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=resume)
    ResumeBtn.place(x=30, y=250)

    PauseBtn = Button(window, text="Pause", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=pause)
    PauseBtn.palce(x=200, y=250)


    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()
