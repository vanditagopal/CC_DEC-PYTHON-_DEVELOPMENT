#MADE BY VANDITA VINAY GOPAL

import tkinter as tk #for gui
import fnmatch #compares file name with pattern and returns true 
from tkinter import *
import os
import pygame
from pygame import *#for playing music and stoping it

#canvas is used to draw ovals polygons etc
canvas=tk.Tk() 
canvas.title("MUSIC PLAYER")
canvas.geometry("500x500")

#image to add in the background
img=PhotoImage(file="F:\\Vinit\Python Codes\music player\\bg3_img.png")
label=Label(canvas,image=img)
label.place(x=0,y=0)

#display listbox to display songs  list
listBox=tk.Listbox(canvas,fg="white",bg="black",width=100,font=("Helvetic",15))
listBox.pack(padx=50,pady=50 )

#file location specified throught rootpath
rootpath="F:\\Vinit\Python Codes\music player"
pattern="*.mp3"
mixer.init() #used for playing audio in pygame
pygame.init()

#image used for player  buttons are initialised
prev_img=tk.PhotoImage(file="prev_img.png")
pause_img=tk.PhotoImage(file="pause_img.png")
play_img=tk.PhotoImage(file="play_img.png")
next_img=tk.PhotoImage(file="next_img.png")

#whenever user selects a song this function will play the song
def select():    
    label.config(text=listBox.get("anchor")) # will get the song name
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

#function to stop or pause the music 
def stop():
    mixer.music.stop()
    listBox.select_clear('active') #clear the song from the listbox 

#function to play the next song
def play_next():
    next_song=listBox.curselection() #curse selection returns the value of the current item in listbox
    next_song=next_song[0]+1 #move on to new index song
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

#function to play previous song
def play_prev():
    next_song=listBox.curselection()
    next_song=next_song[0]-1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

#label to display  song name
label=tk.Label(canvas,text=' ',bg="black",fg="white",font=("Helvetic",10))
label.pack(pady=15)
top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')


#buttons 
prevButton=tk.Button(canvas,text="Prev",image=prev_img,bg="black",borderwidth=0,command=play_prev)
prevButton.pack(padx=15,pady=30,in_=top,side='left')

pauseButton=tk.Button(canvas,text="Pause",image=pause_img,bg="black",borderwidth=0,command=stop)
pauseButton.pack(padx=15,pady=30,in_=top,side='left')

playButton=tk.Button(canvas,text="Play",image=play_img,bg="black",borderwidth=0,command=select)
playButton.pack(padx=15,pady=30,in_=top,side='left')

nextButton=tk.Button(canvas,text="Next",image=next_img,bg="black",borderwidth=0,command=play_next)
nextButton.pack(padx=15,pady=30,in_=top,side='left')


#loop that talks songs from files and inserts it in the listbox
for root ,dirs,files in os.walk(rootpath): #os walk generates the file name in a directory tree 
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)


canvas.mainloop()

