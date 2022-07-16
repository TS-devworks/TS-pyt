#Mp4 to Mp3 / Youtube DL
#Trista Smith
#8 July 2022

import sys
from turtle import bgcolor
from pytube import  YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from tkinter import *
from tkinter import filedialog
import shutil

#functions
def selPath():
    #allows user to search & select dir
    path = filedialog.askdirectory()
    pathLab.config(text=path)

def fileDL():
    #gets user path
    getLnk = link.get()
    #get selected path
    uP = pathLab.cget('text')
    #download video
    mp4V = YouTube(getLnk).streams.get_highest_resolution().download()
    vidClp = VideoFileClip(mp4V)
    vidClp.close()
    #move to user selected dir
    shutil.move(mp4V, uP)
    screen.title('Completed!')

screen = Tk()
title = screen.title('YT Download')
#screen size
canvas = Canvas(screen, width=480, height=500)
canvas.pack()

#add in logo
logopic = PhotoImage(file = './dl_logo.png')
logopic = logopic.subsample(4, 4)
#add to canvas
canvas.create_image(250, 120, image = logopic)

#link entry
link = Entry(screen, width=50)
linklab = Label(screen, text = 'Paste (CTRL+V) Your Link Below: ', font=('Gothic', 13))
#path to save file
pathLab = Label(screen, text='Input Path for File Download', font=('Gothic', 12))
selBtn = Button(screen, text='Select', command=selPath)
#add to canvas
canvas.create_window(250, 340, window = pathLab)
canvas.create_window(250, 370, window = selBtn)


#place widgets in canvas
canvas.create_window(250, 260, window=linklab)
canvas.create_window(250, 280, window=link)

#download button
button = Button(screen, text='Download', command=fileDL)
#add to canvas
canvas.create_window(250, 430, window=button) 


screen.mainloop









#for converter ignore
#ask user to enter/paste mp4/youtube url
user = input('Enter URL you would like to download: ')
print('Downloading...')

#function to download mp4/youtube url

#save mp4 to new mp4 folder w/ auto title {yt_mp4}

#ask if user wants to convert to mp3
user2 = input('Would you like your mp4 file converted? [y/n] ' ).lower()
print('\nPlease wait while your .mp4 file is converting\n')
if user2 == 'y':
    #download new mp3 file to {yt_mp3}
    #prompt if user would like to delete {.mp4 file} [y/n]
    y = input('Would you like to delete your mp4 file? [y/n] ').lower()
    """ for y in input:
        #delete .mp4 file
        print('Deleting....' / 'file deleted' )
 """
else: 
    print('Closing....')
sys.exit()




#def prompt_mp4():
    #download