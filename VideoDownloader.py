# Importações
import pytube as pt
import os
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox

# Variáveis
dir_download = os.environ['USERPROFILE'] + '\Download_Musicas'
dir_mp4 = os.environ['USERPROFILE'] + '\Download_Musicas' + '\mp4'
dir_mp3 = os.environ['USERPROFILE'] + '\Download_Musicas' + '\mp3'

def mp3():
    link = entry.get()
    audio = pt.YouTube(link).streams.get_audio_only()
    title = audio.title
    filename_audio = f'{title}.mp3'
    audio.download(dir_mp3, filename=filename_audio)
    messagebox.showinfo(title='Download realizado com sucesso!', message='Cheque na pasta "C:/Users/[Seu_Usuario]/Download_Musicas/mp3')

def mp4():
    link = entry.get()
    yt = pt.YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download(dir_mp4)
    messagebox.showinfo(title='Download realizado com sucesso!', message='Cheque na pasta "C:/Users/[Seu_Usuario]/Download_Musicas/mp4"')

root = Tk()
root.geometry('500x400')
root.iconbitmap(r'icon.ico')
root.title('VideoDownloader MP3 & MP4')
root.configure(background='#404040')

text1 = Label(root,text = 'Seja muito bem-vind@ ao VideoDownloader MP3 & MP4!', background='ghost white', foreground='#000')
text1.pack(padx=10, pady=10, ipady=20, fill=X, expand=True, side=TOP)

entry = Entry(root, width=50)
entry.pack(padx=10, pady=2, ipady=10, fill=X, expand=True)
entry.insert(0,'Cole aqui o link do video')

b1 = Button(root, text='MP3', command=mp3, bg='#0000FF', fg='ghost white', width= 20, height=4)
b1.pack(padx=10, pady=10, side=TOP)
b2 = Button(root, text='MP4', command=mp4, bg='#000033', fg='ghost white', width= 20, height=4)
b2.pack(padx=10, pady=10, side=TOP)

button_quit = Button(root, text = 'Fechar aplicativo', command=root.quit, background='#990000', foreground='#E0E0E0')
button_quit.pack(padx=10,pady=10,ipady=10, side=RIGHT)

root.mainloop()